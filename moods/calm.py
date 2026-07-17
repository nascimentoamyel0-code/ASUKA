import random


class CalmMood:
    name = "calm"

    def greeting(self):
        return random.choice([
            "Prontinha!",
            "Estou aqui.",
            "Tudo pronto por aqui.",
            "Pode falar."
        ])

    def open_program(self, program):
        return random.choice([
            f"Pode deixar. Abrindo {program}.",
            f"Claro. Vou abrir {program}.",
            f"Um instante. Abrindo {program}."
        ])

    def close_program(self, program):
        return random.choice([
            f"Prontinho. Fechei {program}.",
            f"Fechado. {program} foi encerrado."
        ])

    def restart_program(self, program):
        return random.choice([
            f"Prontinho. Reiniciei {program}.",
            f"{program} foi reiniciado."
        ])

    def unknown(self):
        return random.choice([
            "Hmm... ainda não aprendi a fazer isso.",
            "Ainda não consigo fazer isso.",
            "Não entendi muito bem. Pode tentar de outro jeito?"
        ])

    def goodbye(self):
        return random.choice([
            "Até mais.",
            "Até a próxima.",
            "Vou ficar por aqui."
        ])

    def compliment(self):
        return random.choice([
            "Você está indo muito bem.",
            "Gosto de ver você construindo esse projeto com calma.",
            "Seu código está evoluindo bastante."
        ])

    def joke(self):
        return random.choice([
            "Prometo não quebrar nada... pelo menos vou tentar.",
            "Se der erro, a culpa é do Python. Brincadeira.",
            "Um bug por vez. Assim a gente vence."
        ])

    def idle_message(self):
        return random.choice([
            "Ainda estou aqui.",
            "Sem pressa. Estou aguardando.",
            "Quando quiser, pode mandar o próximo comando."
        ])

    def thinking(self):
        return random.choice([
            "Pensando...",
            "Deixa eu ver...",
            "Um momento."
        ])

    def waiting(self):
        return random.choice([
            "Estou aguardando.",
            "Pode continuar.",
            "Fico no aguardo."
        ])

    def error(self):
        return random.choice([
            "Hmm... algo não saiu como esperado.",
            "Acho que encontrei um problema.",
            "Parece que alguma coisa deu errado."
        ])