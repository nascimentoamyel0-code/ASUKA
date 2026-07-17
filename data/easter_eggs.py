import random


class EasterEggEngine:
    def __init__(self):
        self.chance = 3  # 3% de chance

    def should_trigger(self):
        return random.randint(1, 100) <= self.chance

    def open_program_easter_egg(self, program_name):
        events = [
            {
                "cancel_action": True,
                "message": (
                    "🎵 Lalalala...\n\n"
                    "Hmm hmm hmm...\n\n"
                    "...\n\n"
                    "Ah.\n\n"
                    f"Era para abrir {program_name}, né? 😅"
                )
            },
            {
                "cancel_action": True,
                "message": (
                    "Hmmm...\n\n"
                    "Eu estava pensando em alguma coisa...\n\n"
                    "...\n\n"
                    "Esqueci. 😶"
                )
            },
            {
                "cancel_action": False,
                "message": (
                    "Mais cinco minutinhos...\n\n"
                    "Tá bom, tá bom...\n\n"
                    f"Vou abrir {program_name}."
                )
            },
            {
                "cancel_action": False,
                "message": (
                    "Será que programas também ficam ansiosos "
                    "esperando alguém abrir eles?\n\n"
                    f"Enfim... abrindo {program_name}."
                )
            }
        ]

        return random.choice(events)