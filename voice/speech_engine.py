import json
from pathlib import Path
from rapidfuzz import process, fuzz


class SpeechEngine:
    def __init__(self):
        self.base_path = Path("voice/speech")
        self.plugins_path = Path("plugins/programs")

        self.corrections = self.load_json("corrections.json", {})
        self.aliases = self.load_json("aliases.json", {})
        self.ignored_words = self.load_json("ignored_words.json", [])
        self.wake_words = self.load_json("wake_words.json", [])

        self.programs = self.load_programs_from_plugins()

        self.actions = {
            "abrir": [
                "abrir", "abre", "abra", "abri", "abril", "abrirr",
                "iniciar", "inicia", "executar", "executa"
            ],
            "fechar": [
                "fechar", "fecha", "feche", "encerrar", "encerra",
                "finalizar", "finaliza"
            ],
            "reiniciar": [
                "reiniciar", "reinicia", "reinicie", "reabrir",
                "reabre", "abrir novamente", "abre novamente"
            ]
        }

    def load_json(self, filename, default):
        file_path = self.base_path / filename

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

            programs[program_id] = list(set(alias.lower() for alias in aliases if alias))

        return programs

    def normalize(self, text):
        text = text.lower().strip()

        for char in [".", ",", "!", "?", ":", ";", "-", "_"]:
            text = text.replace(char, " ")

        text = self.apply_corrections(text)
        text = self.apply_aliases(text)
        text = self.remove_ignored_words(text)
        text = " ".join(text.split())

        text = self.fuzzy_normalize(text)

        return text

    def apply_corrections(self, text):
        corrections = sorted(
            self.corrections.items(),
            key=lambda item: len(item[0]),
            reverse=True
        )

        for wrong, correct in corrections:
            text = text.replace(wrong, correct)

        return text

    def apply_aliases(self, text):
        for official, variants in self.aliases.items():
            for variant in variants:
                text = text.replace(variant, official)

        return text

    def remove_ignored_words(self, text):
        words = text.split()

        cleaned_words = [
            word for word in words
            if word not in self.ignored_words
        ]

        return " ".join(cleaned_words)

    def fuzzy_normalize(self, text):
        words = text.split()
        normalized_words = []

        for word in words:
            action = self.match_action(word)

            if action:
                normalized_words.append(action)
                continue

            program = self.match_program(word)

            if program:
                normalized_words.append(program)
                continue

            normalized_words.append(word)

        return " ".join(normalized_words)

    def match_action(self, word):
        all_action_words = []

        for action, variants in self.actions.items():
            for variant in variants:
                all_action_words.append((variant, action))

        choices = [item[0] for item in all_action_words]

        match = process.extractOne(
            word,
            choices,
            scorer=fuzz.ratio
        )

        if not match:
            return None

        matched_word, score, _ = match

        if score < 78:
            return None

        for variant, action in all_action_words:
            if variant == matched_word:
                return action

        return None

    def match_program(self, word):
        choices = []

        for program_id, aliases in self.programs.items():
            for alias in aliases:
                choices.append((alias, program_id))

        if not choices:
            return None

        alias_list = [item[0] for item in choices]

        match = process.extractOne(
            word,
            alias_list,
            scorer=fuzz.ratio
        )

        if not match:
            return None

        matched_alias, score, _ = match

        if score < 65:
            return None

        for alias, program_id in choices:
            if alias == matched_alias:
                return program_id

        return None

    def extract_wake_command(self, text):
        text = text.lower().strip()

        for char in [".", ",", "!", "?", ":", ";"]:
            text = text.replace(char, "")

        words = text.split()

        if not words:
            return None

        first_word = words[0]

        wake_match = process.extractOne(
            first_word,
            self.wake_words,
            scorer=fuzz.ratio
        )

        if wake_match:
            wake_word, score, _ = wake_match

            if score >= 65:
                command = " ".join(words[1:])
                return self.normalize(command)

        normalized = self.normalize(text)

        for wake_word in self.wake_words:
            if normalized.startswith(wake_word):
                return normalized.replace(wake_word, "", 1).strip()

        return None