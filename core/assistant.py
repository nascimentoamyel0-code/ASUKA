from core.speaker import Speaker
from core.brain import Brain
from core.listener import Listener

from commands.program_manager import ProgramManager

from data.personality import Personality
from data.statistics import StatisticsEngine
from data.sessions import SessionEngine
from data.context import ContextEngine
from data.knowledge import KnowledgeEngine

from voice.speech_engine import SpeechEngine
from voice.voice_state import VoiceState

from services.pokemon.pokeapi_service import PokeApiService


class Assistant:
    def __init__(self):
        self.name = "Asuka"
        self.version = "0.6.1"

        self.speaker = Speaker()
        self.listener = Listener()
        self.brain = Brain()

        self.program_manager = ProgramManager()
        self.personality = Personality()
        self.statistics = StatisticsEngine()
        self.session_engine = SessionEngine()
        self.context = ContextEngine()
        self.knowledge = KnowledgeEngine()

        self.speech_engine = SpeechEngine()
        self.voice_state = VoiceState()

        self.pokeapi = PokeApiService()

    def start(self):
        print("=" * 50)
        print(f"          {self.name} v{self.version}")
        print("=" * 50)

        print("\nInicializando...\n")
        self.speaker.say(self.personality.greeting())

        for message in self.context.startup_messages():
            self.speaker.say(message)

        while True:
            command = self.get_command()

            if not command:
                continue

            self.personality.register_command()

            if command.lower() in ["sair", "encerrar", "fechar asuka"]:
                self.handle_exit()
                break

            if command.lower() in ["modo voz", "ativar voz", "voz contínua", "voz continua"]:
                self.voice_state.set_idle()
                self.speaker.say("Modo voz ativado. Pode me chamar quando quiser.")
                print("💤 Asuka está aguardando a palavra de ativação...")
                continue

            if command.lower() in ["modo texto", "desativar voz", "parar voz"]:
                self.voice_state.set_text_mode()
                self.speaker.say("Modo texto ativado.")
                continue

            self.process_command(command)

    def get_command(self):
        if self.voice_state.is_text():
            command = input("\nVocê: ")

            if command.lower() in ["ouvir", "escutar"]:
                heard = self.listener.listen()

                if not heard:
                    self.speaker.say("Não entendi muito bem... pode repetir?")
                    return None

                print(f"\nVocê disse: {heard}")
                return heard

            return command

        heard = self.listener.listen()

        if not heard:
            return None

        print(f"\nVocê disse: {heard}")

        if self.voice_state.is_idle():
            command = self.speech_engine.extract_wake_command(heard)

            if not command:
                print("💤 Asuka está aguardando a palavra de ativação...")
                return None

            self.voice_state.set_conversation()
            self.speaker.say("Oi! Pode falar.")

            if command:
                print(f"Comando ativado: {command}")
                return command

            return None

        if self.voice_state.is_conversation():
            if self.voice_state.conversation_expired():
                self.voice_state.set_idle()
                self.speaker.say("Vou ficar por aqui. Me chama quando precisar.")
                print("💤 Asuka voltou a descansar.")
                return None

            self.voice_state.refresh_conversation()
            return heard

        return None

    def process_command(self, command):
        intent = self.brain.think(command)

        action = intent["action"]
        target = intent["target"]

        if action == "open":
            self.handle_open(target)

        elif action == "close":
            self.handle_close(target)

        elif action == "restart":
            self.handle_restart(target)

        elif action == "joke":
            self.handle_joke()

        elif action == "compliment":
            self.handle_compliment()

        elif action == "show_mood":
            self.handle_show_mood()

        elif action == "set_mood":
            self.handle_set_mood(target)

        elif action == "statistics":
            self.handle_statistics()

        elif action == "achievements":
            self.handle_achievements()

        elif action == "remember":
            self.handle_remember(target)

        elif action == "recall":
            self.handle_recall(target)

        elif action == "list_memories":
            self.handle_list_memories()

        elif action == "conversation":
            self.handle_conversation(target)

        elif action == "pokemon_info":
            self.handle_pokemon_info(target)

        else:
            self.handle_unknown()

        self.handle_after_command()

    def handle_open(self, target):
        program_data = self.program_manager.get_program_data(target)

        if not program_data:
            self.speaker.say(self.personality.error_open(target))
            return

        response = self.personality.open_program(program_data["name"])
        self.speaker.say(response["message"])

        if response["cancel_action"]:
            return

        result = self.program_manager.open(target)

        if result["success"]:
            if result.get("already_running"):
                self.speaker.say(
                    self.personality.already_open(result["name"])
                )
            else:
                self.personality.register_program_opened(result["name"])
            return

        if result.get("reason") == "path_not_found":
            exe_name = result.get("exe_name")

            self.speaker.say(
                f"Hmm... acho que o {result['name']} mudou de lugar."
            )

            self.speaker.say(
                f"Vou tentar encontrar o arquivo {exe_name}. Em qual disco devo procurar?"
            )

            drive = input("\nDisco para escanear: ").strip().replace(":", "")

            if not drive:
                self.speaker.say("Tudo bem. Não vou procurar agora.")
                return

            self.speaker.say(
                f"Procurando no disco {drive}: ... isso pode demorar um pouco."
            )

            repair_result = self.program_manager.repair_path(
                target,
                [drive]
            )

            if repair_result["success"]:
                self.speaker.say(
                    "Encontrei! Atualizei minha memória com o novo caminho."
                )

                new_result = self.program_manager.open(target)

                if new_result["success"]:
                    self.speaker.say(
                        f"Agora consegui abrir {result['name']}."
                    )
                else:
                    self.speaker.say(
                        self.personality.error_open(result["name"])
                    )

            else:
                self.speaker.say(
                    f"Não encontrei o {exe_name} no disco {drive}."
                )

            return

        self.speaker.say(
            self.personality.error_open(result["name"])
        )

    def handle_close(self, target):
        result = self.program_manager.close(target)

        if result["success"]:
            if result.get("already_closed"):
                self.speaker.say(
                    self.personality.already_closed(result["name"])
                )
            else:
                self.speaker.say(
                    self.personality.close_program(result["name"])
                )
        else:
            self.speaker.say(
                self.personality.error_close(result["name"])
            )

    def handle_restart(self, target):
        result = self.program_manager.restart(target)

        if result["success"]:
            self.personality.register_program_opened(result["name"])
            self.speaker.say(
                self.personality.restart_program(result["name"])
            )
        else:
            self.speaker.say(
                self.personality.error_restart(result["name"])
            )

    def handle_joke(self):
        self.speaker.say(
            self.personality.joke()
        )

    def handle_compliment(self):
        self.speaker.say(
            self.personality.compliment()
        )

    def handle_show_mood(self):
        mood = self.personality.mood_engine.current_mood_name

        self.speaker.say(
            f"Meu humor atual é: {mood}."
        )

    def handle_set_mood(self, target):
        success = self.personality.mood_engine.set_mood(target)

        if success:
            self.speaker.say(
                f"Prontinho! Agora estou no modo {target}."
            )
        else:
            self.speaker.say(
                "Hmm... não conheço esse humor."
            )

    def handle_statistics(self):
        self.speaker.say(
            self.statistics.summary()
        )

    def handle_achievements(self):
        self.speaker.say(
            self.context.achievements.list_unlocked()
        )

    def handle_remember(self, target):
        self.knowledge.remember(
            target["key"],
            target["value"]
        )

        self.speaker.say(
            f"Prontinho. Vou lembrar que {target['key']} é {target['value']}."
        )

    def handle_recall(self, target):
        value = self.knowledge.recall(target)

        if value:
            feminine_words = [
                "comida",
                "linguagem",
                "cor",
                "cidade",
                "música",
                "musica",
                "série",
                "serie"
            ]

            article = "Seu"

            for word in feminine_words:
                if target.startswith(word):
                    article = "Sua"
                    break

            self.speaker.say(
                f"{article} {target} é {value}."
            )
        else:
            self.speaker.say(
                "Hmm... não lembro disso ainda."
            )

    def handle_list_memories(self):
        facts = self.knowledge.list_facts()

        if not facts:
            self.speaker.say(
                "Ainda não tenho memórias salvas sobre você."
            )
            return

        lines = ["Eu lembro dessas coisas sobre você:"]

        for key, value in facts.items():
            lines.append(f"- {key}: {value}")

        self.speaker.say(
            "\n".join(lines)
        )

    def handle_conversation(self, target):
        self.speaker.say(target)

    def handle_pokemon_info(self, target):
        pokemon = self.pokeapi.get_pokemon(target)

        if not pokemon:
            self.speaker.say(f"Hmm... não encontrei informações sobre {target}.")
            return

        if pokemon.get("scan_text"):
            self.speaker.say(pokemon["scan_text"])
            return

        types = ", ".join(pokemon["types"])
        abilities = ", ".join(pokemon["abilities"])
        stats = pokemon["stats"]

        message = (
            f"{pokemon['name'].title()} é do tipo {types}. "
            f"Suas habilidades são: {abilities}. "
            f"Stats base: HP {stats['hp']}, Ataque {stats['attack']}, "
            f"Defesa {stats['defense']}, Ataque Especial {stats['special-attack']}, "
            f"Defesa Especial {stats['special-defense']} e Velocidade {stats['speed']}."
        )

        self.speaker.say(message)

    def handle_unknown(self):
        self.speaker.say(
            self.personality.unknown()
        )

    def handle_after_command(self):
        for message in self.context.after_command_messages():
            self.speaker.say(message)

    def handle_exit(self):
        minutes = self.session_engine.end_session()

        self.speaker.say(
            self.personality.goodbye()
        )

        self.speaker.say(
            f"Essa sessão durou {minutes} minuto(s)."
        )