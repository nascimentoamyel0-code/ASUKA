import random


class PlayfulMood:
    name = "playful"

    def greeting(self):
        return random.choice([
            "Prontinha! Qual é a missão de hoje?",
            "Oi! Prometo tentar não me distrair.",
            "Estou aqui! Pode mandar."
        ])

    def open_program(self, program):
        return random.choice([
            f"Tá bom, tá bom... abrindo {program}.",
            f"Vamos lá! Abrindo {program}.",
            f"Espero que isso não vire madrugada, hein. Abrindo {program}."
        ])

    def close_program(self, program):
        return random.choice([
            f"Fechei {program}. Adeus, guerreiro.",
            f"Prontinho! {program} foi fechado.",
            f"{program} encerrado com sucesso dramático."
        ])

    def restart_program(self, program):
        return random.choice([
            f"Reiniciando {program}. Às vezes todo mundo precisa de um recomeço.",
            f"Prontinho! Dei um reset em {program}.",
            f"{program} foi reiniciado. Agora vai!"
        ])

    def unknown(self):
        return random.choice([
            "Hmm... isso ainda está fora do meu treinamento secreto.",
            "Ainda não aprendi isso, mas gostei da ousadia.",
            "Não entendi... mas vou fingir que foi profundo."
        ])

    def goodbye(self):
        return random.choice([
            "Até mais! Tente não quebrar o código sem mim.",
            "Tchau! Vou fingir que estou descansando.",
            "Até depois! Se der bug, você sabe onde me encontrar."
        ])

    def compliment(self):
        return random.choice([
            "Você está ficando perigoso nesse Python, hein.",
            "Esse projeto está ganhando cara de coisa séria.",
            "A Asuka aprova esse progresso."
        ])

    def joke(self):
        return random.choice([
            "Se aparecer erro, a gente chama de feature experimental.",
            "Meu plano era dominar o computador... mas abrir a Steam já está ótimo.",
            "Prometo não cantarolar agora. Talvez."
        ])

    def idle_message(self):
        return random.choice([
            "Estou aqui... tentando não mexer em nada.",
            "Silêncio suspeito detectado.",
            "Se quiser, eu posso fingir que estou ocupada."
        ])

    def thinking(self):
        return random.choice([
            "Pensando... com estilo.",
            "Deixa eu consultar meus parafusos imaginários.",
            "Analisando... quase dramaticamente."
        ])

    def waiting(self):
        return random.choice([
            "Manda a próxima missão.",
            "Estou pronta para causar... digo, ajudar.",
            "Pode falar."
        ])

    def error(self):
        return random.choice([
            "Ops... tropecei num bug.",
            "Alguma coisa deu errado. Foi mal, chefe.",
            "Erro detectado. Culpa minha? Talvez."
        ])