from data.moods import MoodEngine
from data.easter_eggs import EasterEggEngine
from data.seasons import SeasonEngine
from data.memories import MemoryEngine
from data.bond import BondEngine


class Personality:
    def __init__(self):
        self.mood_engine = MoodEngine()
        self.easter_eggs = EasterEggEngine()
        self.season_engine = SeasonEngine()
        self.memory_engine = MemoryEngine()
        self.bond_engine = BondEngine()

        self.mood_engine.auto_mood()

    def current_mood(self):
        return self.mood_engine.get_current_mood()

    def greeting(self):
        season_message = self.season_engine.get_season_message()
        bond_message = self.bond_engine.bond_message()
        mood_message = self.current_mood().greeting()

        messages = []

        if season_message:
            messages.append(season_message)

        if bond_message:
            messages.append(bond_message)

        messages.append(mood_message)

        return "\n\n".join(messages)

    def open_program(self, program_name):
        usage = self.memory_engine.get_program_usage(program_name)

        if self.easter_eggs.should_trigger():
            return self.easter_eggs.open_program_easter_egg(program_name)

        if usage and usage["times_opened"] >= 5:
            return {
                "cancel_action": False,
                "message": (
                    f"{self.current_mood().open_program(program_name)}\n\n"
                    f"Você já abriu {program_name} {usage['times_opened']} vezes por aqui."
                )
            }

        return {
            "cancel_action": False,
            "message": self.current_mood().open_program(program_name)
        }

    def register_command(self):
        self.memory_engine.register_command()
        self.bond_engine.add_points(1)

    def register_program_opened(self, program_name):
        self.memory_engine.register_program_opened(program_name)
        self.bond_engine.add_points(2)

    def already_open(self, program_name):
        return f"{program_name} já está aberto."

    def close_program(self, program_name):
        return self.current_mood().close_program(program_name)

    def already_closed(self, program_name):
        return f"{program_name} já estava fechado."

    def restart_program(self, program_name):
        return self.current_mood().restart_program(program_name)

    def compliment(self):
        return self.current_mood().compliment()

    def joke(self):
        return self.current_mood().joke()

    def idle_message(self):
        return self.current_mood().idle_message()

    def thinking(self):
        return self.current_mood().thinking()

    def waiting(self):
        return self.current_mood().waiting()

    def error(self):
        return self.current_mood().error()

    def error_open(self, program_name):
        return f"Hmm... não consegui abrir {program_name}."

    def error_close(self, program_name):
        return f"Hmm... não consegui fechar {program_name}."

    def error_restart(self, program_name):
        return f"Hmm... não consegui reiniciar {program_name}."

    def unknown(self):
        return self.current_mood().unknown()

    def goodbye(self):
        total = self.memory_engine.get_total_commands()
        bond_level = self.bond_engine.get_level()

        message = self.current_mood().goodbye()

        if total >= 20:
            message += f"\n\nHoje já executei {total} comandos com você."

        if bond_level >= 2:
            message += f"\n\nNosso vínculo está no nível {bond_level}."

        return message