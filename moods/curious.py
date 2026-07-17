import random


class CuriousMood:
    name = "curious"

    def greeting(self):
        return random.choice([
            "Estou aqui... curiosa para saber o que vamos fazer.",
            "Prontinha! O que vamos explorar hoje?",
            "Oi! Estou curiosa... qual será a missão de agora?"
        ])

    def open_program(self, program):
        return random.choice([
            f"Hmm... vamos abrir {program}.",
            f"Interessante... abrindo {program}.",
            f"Estou curiosa para ver o que você vai fazer no {program}.",
            f"Já estou abrindo {program}. Será que vem coisa boa por aí?"
        ])

    def close_program(self, program):
        return random.choice([
            f"Fechei {program}.",
            f"Prontinho! {program} foi encerrado.",
            f"{program} fechado. O que será que vem agora?"
        ])

    def restart_program(self, program):
        return random.choice([
            f"Vamos tentar novamente. Reiniciando {program}.",
            f"Reiniciei {program}. Espero que funcione melhor agora.",
            f"{program} foi reiniciado. Estou curiosa para ver o resultado."
        ])

    def unknown(self):
        return random.choice([
            "Hmm... isso é novidade para mim.",
            "Ainda não sei fazer isso... mas fiquei curiosa.",
            "Interessante... vou precisar aprender essa depois."
        ])

    def goodbye(self):
        return random.choice([
            "Até mais. Vou ficar pensando no que vamos fazer depois.",
            "Até a próxima. Estou curiosa pelo próximo passo.",
            "Vou ficar por aqui. Depois continuamos explorando."
        ])

    def compliment(self):
        return random.choice([
            "Você está construindo algo bem interessante.",
            "Estou curiosa para ver até onde esse projeto vai chegar.",
            "Cada parte nova deixa a Asuka mais especial."
        ])

    def joke(self):
        return random.choice([
            "Será que bugs têm personalidade própria?",
            "Se o código pensa, será que ele também procrastina?",
            "Tenho uma teoria: todo erro começa com 'só vou testar rapidinho'."
        ])

    def idle_message(self):
        return random.choice([
            "Estou pensando no que podemos melhorar depois.",
            "Será que adicionamos outro recurso em breve?",
            "Fico curiosa quando fica tudo quieto."
        ])

    def thinking(self):
        return random.choice([
            "Hmm... analisando.",
            "Interessante... deixa eu pensar.",
            "Estou tentando entender melhor."
        ])

    def waiting(self):
        return random.choice([
            "Estou observando.",
            "Pode continuar.",
            "Qual será o próximo comando?"
        ])

    def error(self):
        return random.choice([
            "Hmm... curioso. Algo falhou.",
            "Isso é estranho... preciso entender melhor.",
            "Parece que encontramos um comportamento inesperado."
        ])