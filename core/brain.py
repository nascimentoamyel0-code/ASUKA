import json
from pathlib import Path

from core.normalizer import Normalizer
from core.parser import Parser


class Brain:
    def __init__(self):
        self.plugins_path = Path("plugins/programs")

        self.normalizer = Normalizer()
        self.parser = Parser()

        self.programs = self.load_programs_from_plugins()
        self.commands = self.load_json("voice/speech/commands.json", {})
        self.ignored_words = self.load_json("voice/speech/ignored_words.json", [])

        self.min_confidence = 72

    def load_json(self, path, default):
        file_path = Path(path)

        if not file_path.exists():
            return default

        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def load_programs_from_plugins(self):
        programs = {}

        if not self.plugins_path.exists():
            return programs

        for file in self.plugins_path.glob("*.json"):
            with open(file, "r", encoding="utf-8") as f:
                data = json.load(f)

            program_id = data.get("id", file.stem).lower()

            aliases = data.get("aliases", [])
            aliases.append(program_id)
            aliases.append(data.get("name", "").lower())

            aliases = list(set(
                alias.lower().strip()
                for alias in aliases
                if alias and alias.strip()
            ))

            programs[program_id] = aliases

        return programs

    def clean_command(self, command):
        return self.normalizer.normalize(command)

    def build_action_options(self):
        options = {}

        for action, phrases in self.commands.items():
            for phrase in phrases:
                phrase = self.normalizer.normalize(phrase)

                if phrase:
                    options[phrase] = action

        return options

    def build_program_options(self):
        options = {}

        for program_id, aliases in self.programs.items():
            for alias in aliases:
                alias = self.normalizer.normalize(alias)

                if alias:
                    options[alias] = program_id

        return options

    def find_action_and_program(self, command):
        action_options = self.build_action_options()
        program_options = self.build_program_options()

        result = self.parser.parse(
            command,
            action_options,
            program_options
        )

        print("[PARSER]", result)

        if (
            result["action"]
            and result["target"]
            and result["confidence"] >= self.min_confidence
        ):
            return {
                "action": result["action"],
                "target": result["target"]
            }

        return None

    def detect_pokemon_question(self, command):
        triggers = [
            "pokemon",
            "me fala sobre",
            "me fale sobre",
            "fale me sobre",
            "me diga sobre" ,
            "informacoes sobre",
            "informações sobre",
            "fale sobre",
            "pesquisa",
            "pesquise",
            "procura",
            "procure",
            "tipo",
            "tipos",
            "tipo de",
            "tipos de",
            "quem e",
            "quem eh",
            "quem é",
            "stats",
            "status",
            "habilidade",
            "habilidades"
        ]

        for trigger in triggers:
            if command.startswith(trigger):
                target = command.replace(trigger, "", 1).strip()

                if target:
                    return {
                        "action": "pokemon_info",
                        "target": target
                    }

        return None

    def think(self, command):
        command = self.clean_command(command)

        print(f"[DEBUG] Comando limpo: {command}")

        if command in [
            "estatisticas",
            "estatísticas",
            "stats",
            "minhas estatisticas",
            "minhas estatísticas"
        ]:
            return {"action": "statistics", "target": None}

        if command in [
            "conquistas",
            "minhas conquistas",
            "achievements"
        ]:
            return {"action": "achievements", "target": None}

        if command in [
            "o que voce sabe sobre mim",
            "que voce sabe sobre mim",
            "listar memorias",
            "minhas memorias"
        ]:
            return {"action": "list_memories", "target": None}

        if command in [
            "piada",
            "conte piada",
            "conte uma piada",
            "me conte piada",
            "me conte uma piada",
            "me faz rir"
        ]:
            return {"action": "joke", "target": None}

        if command in [
            "elogio",
            "me elogie",
            "fala algo legal"
        ]:
            return {"action": "compliment", "target": None}

        if command in [
            "mood",
            "humor",
            "qual seu humor"
        ]:
            return {"action": "show_mood", "target": None}

        if command.startswith("mood "):
            return {
                "action": "set_mood",
                "target": command.replace("mood ", "").strip()
            }

        if command.startswith("humor "):
            return {
                "action": "set_mood",
                "target": command.replace("humor ", "").strip()
            }

        if command.startswith("lembre que "):
            fact = command.replace("lembre que ", "").strip()

            if " e " in fact or " é " in fact:
                if " e " in fact:
                    key, value = fact.split(" e ", 1)
                else:
                    key, value = fact.split(" é ", 1)

                key = key.strip()
                value = value.strip()

                if key.startswith("meu "):
                    key = key.replace("meu ", "", 1)

                if key.startswith("minha "):
                    key = key.replace("minha ", "", 1)

                return {
                    "action": "remember",
                    "target": {
                        "key": key,
                        "value": value
                    }
                }

        if command.startswith("qual "):
            key = command.replace("qual ", "").replace("?", "").strip()

            if key.startswith("meu "):
                key = key.replace("meu ", "", 1)

            if key.startswith("minha "):
                key = key.replace("minha ", "", 1)

            return {
                "action": "recall",
                "target": key
            }

        pokemon_intent = self.detect_pokemon_question(command)

        if pokemon_intent:
            return pokemon_intent

        intent = self.find_action_and_program(command)

        if intent:
            return intent

        return {
            "action": "conversation",
            "target": "Hmm... eu não tenho certeza do que você quis dizer. Pode falar de outro jeito?"
        }