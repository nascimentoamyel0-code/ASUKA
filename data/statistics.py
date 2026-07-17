from data.memories import MemoryEngine


class StatisticsEngine:
    def __init__(self):
        self.memory = MemoryEngine()

    def get_most_used_program(self):
        usage = self.memory.memories.get("program_usage", {})

        if not usage:
            return None

        return max(
            usage.items(),
            key=lambda item: item[1]["times_opened"]
        )

    def summary(self):
        total_commands = self.memory.get_total_commands()
        last_program = self.memory.get_last_program_opened()
        most_used = self.get_most_used_program()

        lines = [
            "📊 Estatísticas da Asuka",
            "",
            f"Comandos executados: {total_commands}"
        ]

        if last_program:
            lines.append(f"Último programa aberto: {last_program}")

        if most_used:
            program_name, data = most_used
            lines.append(
                f"Programa mais usado: {program_name} ({data['times_opened']} vezes)"
            )

        if not most_used:
            lines.append("Ainda não tenho programas registrados.")

        return "\n".join(lines)