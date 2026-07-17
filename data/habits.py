from data.memories import MemoryEngine


class HabitEngine:
    def __init__(self):
        self.memory = MemoryEngine()

    def most_used_program(self):
        usage = self.memory.memories.get("program_usage", {})

        if not usage:
            return None

        return max(
            usage.items(),
            key=lambda item: item[1]["times_opened"]
        )

    def habit_message(self):
        most_used = self.most_used_program()

        if not most_used:
            return None

        program_name, data = most_used
        times = data["times_opened"]

        if times >= 50:
            return f"{program_name} já virou praticamente parte da sua rotina."

        if times >= 20:
            return f"Percebi que você usa bastante o {program_name}."

        if times >= 10:
            return f"{program_name} está começando a aparecer bastante por aqui."

        return None