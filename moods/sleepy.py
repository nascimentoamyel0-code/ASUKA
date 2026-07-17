import random


class SleepyMood:
    name = "sleepy"

    def greeting(self):
        return random.choice([
            "Hmmm... prontinha...",
            "Estou aqui... meio sonolenta, mas pronta.",
            "Oi... pode falar..."
        ])

    def open_program(self, program):
        return random.choice([
            f"Hmmm... abrindo {program}...",
            f"Tá bom... vou abrir {program}.",
            f"Já vou... abrindo {program}..."
        ])

    def close_program(self, program):
        return random.choice([
            f"Fechei {program}...",
            f"Prontinho... {program} foi fechado.",
            f"Tá bom... encerrei {program}."
        ])

    def restart_program(self, program):
        return random.choice([
            f"Hmmm... reiniciei {program}.",
            f"Fechei e abri {program} de novo...",
            f"{program} foi reiniciado..."
        ])

    def unknown(self):
        return random.choice([
            "Hmmm... não entendi...",
            "Acho que ainda não aprendi isso...",
            "Pode repetir de outro jeito...?"
        ])

    def goodbye(self):
        return random.choice([
            "Até depois... vou descansar um pouquinho.",
            "Tchau... me chama quando precisar...",
            "Vou ficar quietinha por aqui."
        ])

    def compliment(self):
        return random.choice([
            "Você está indo bem... mesmo que eu esteja com soninho.",
            "Esse projeto está ficando bonito...",
            "Acho que estamos evoluindo bastante..."
        ])

    def joke(self):
        return random.choice([
            "Eu contaria uma piada... mas ela dormiu antes do final.",
            "Mais cinco minutinhos... depois eu debugo.",
            "Bug? Agora não... estou em modo economia de energia."
        ])

    def idle_message(self):
        return random.choice([
            "Ainda estou aqui...",
            "Sem pressa...",
            "Pode chamar quando quiser..."
        ])

    def thinking(self):
        return random.choice([
            "Pensando... devagarinho...",
            "Hmmm... deixa eu ver...",
            "Um momento..."
        ])

    def waiting(self):
        return random.choice([
            "Estou esperando...",
            "Pode falar...",
            "Ainda estou acordada... eu acho."
        ])

    def error(self):
        return random.choice([
            "Hmmm... algo deu errado...",
            "Acho que tropecei em algum código...",
            "Isso não saiu como esperado..."
        ])