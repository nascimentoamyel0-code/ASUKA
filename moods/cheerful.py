import random


class CheerfulMood:
    name = "cheerful"

    def greeting(self):
        return random.choice([
            "Prontinha! 😄",
            "Oi! Tudo pronto por aqui!",
            "Estou aqui! O que vamos fazer hoje?"
        ])

    def open_program(self, program):
        return random.choice([
            f"Oba! Abrindo {program}.",
            f"Pode deixar! Abrindo {program}.",
            f"Já estou indo! Abrindo {program}."
        ])

    def close_program(self, program):
        return random.choice([
            f"Prontinho! Fechei {program}.",
            f"Fechado! {program} foi encerrado.",
            f"Missão cumprida! Fechei {program}."
        ])

    def restart_program(self, program):
        return random.choice([
            f"Prontinho! Reiniciei {program}.",
            f"Tudo certo! {program} foi reiniciado.",
            f"Fechei e abri {program} de novo!"
        ])

    def unknown(self):
        return random.choice([
            "Hmm... ainda não aprendi isso, mas posso aprender depois!",
            "Essa habilidade ainda está em desenvolvimento!",
            "Não entendi, mas gostei da ideia!"
        ])

    def goodbye(self):
        return random.choice([
            "Até mais! 💙",
            "Até a próxima! Foi bom ajudar.",
            "Vou ficar por aqui. Me chama quando precisar!"
        ])

    def compliment(self):
        return random.choice([
            "Você está mandando muito bem!",
            "Esse projeto está ficando incrível!",
            "A Asuka está evoluindo graças a você. 😄"
        ])

    def joke(self):
        return random.choice([
            "Eu ia contar uma piada de programação, mas ela deu erro de sintaxe.",
            "Por que o Python foi ao médico? Porque estava com indentação quebrada.",
            "Eu prometo não cantarolar... por enquanto."
        ])

    def idle_message(self):
        return random.choice([
            "Estou aqui, prontinha!",
            "Qual será a próxima missão?",
            "Sem pressa! Estou animada para continuar."
        ])

    def thinking(self):
        return random.choice([
            "Pensando rapidinho!",
            "Deixa comigo!",
            "Hmm... já estou vendo isso."
        ])

    def waiting(self):
        return random.choice([
            "Pode mandar!",
            "Estou pronta!",
            "Só dizer o que fazemos agora."
        ])

    def error(self):
        return random.choice([
            "Ops... acho que alguma coisa tropeçou aqui.",
            "Eita... isso não saiu como planejado.",
            "Hmm... pequeno problema detectado!"
        ])