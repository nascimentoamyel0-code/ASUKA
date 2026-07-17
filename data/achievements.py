import json
import os

from data.memories import MemoryEngine
from data.sessions import SessionEngine
from data.bond import BondEngine


class AchievementEngine:
    def __init__(self):
        self.file_path = "data/achievements.json"

        self.memory = MemoryEngine()
        self.sessions = SessionEngine()
        self.bond = BondEngine()

        self.data = self.load()

        self.catalog = {
            "commands_10": "Primeiros 10 comandos",
            "commands_50": "Aquecendo os circuitos",
            "commands_100": "Usuário frequente",
            "commands_500": "Maratonista de comandos",
            "first_program": "Primeiro programa aberto",
            "vscode_10": "Pequeno programador",
            "vscode_50": "Programador dedicado",
            "steam_10": "Hora da diversão",
            "spotify_10": "Trilha sonora ativa",
            "tlauncher_10": "Treinador em jornada",
            "pcsx2_10": "Nostalgia desbloqueada",
            "parsec_10": "Conexão remota",
            "session_1": "Primeira sessão registrada",
            "session_10": "Rotina com a Asuka",
            "time_60": "Uma hora juntos",
            "time_300": "Cinco horas de parceria",
            "bond_1": "Primeiro vínculo",
            "bond_3": "Familiaridade crescente",
            "bond_5": "Companheiros de jornada"
        }

    def load(self):
        if not os.path.exists(self.file_path):
            data = {"unlocked": []}
            self.save(data)
            return data

        with open(self.file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def save(self, data=None):
        if data is None:
            data = self.data

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def unlock(self, achievement_id, title):
        if achievement_id in self.data["unlocked"]:
            return None

        self.data["unlocked"].append(achievement_id)
        self.save()

        return f"🏆 Conquista desbloqueada: {title}"

    def list_unlocked(self):
        unlocked = self.data.get("unlocked", [])

        if not unlocked:
            return "Você ainda não desbloqueou conquistas."

        lines = ["🏆 Conquistas desbloqueadas:"]

        for achievement_id in unlocked:
            title = self.catalog.get(achievement_id, achievement_id)
            lines.append(f"- {title}")

        return "\n".join(lines)

    def program_times(self, program_name):
        usage = self.memory.memories.get("program_usage", {})
        program = usage.get(program_name)

        if not program:
            return 0

        return program.get("times_opened", 0)

    def check(self):
        total_commands = self.memory.get_total_commands()
        last_program = self.memory.get_last_program_opened()
        total_sessions = self.sessions.get_total_sessions()
        total_minutes = self.sessions.get_total_minutes()
        bond_level = self.bond.get_level()

        checks = []

        if total_commands >= 10:
            checks.append(self.unlock("commands_10", self.catalog["commands_10"]))

        if total_commands >= 50:
            checks.append(self.unlock("commands_50", self.catalog["commands_50"]))

        if total_commands >= 100:
            checks.append(self.unlock("commands_100", self.catalog["commands_100"]))

        if total_commands >= 500:
            checks.append(self.unlock("commands_500", self.catalog["commands_500"]))

        if last_program:
            checks.append(self.unlock("first_program", self.catalog["first_program"]))

        if self.program_times("Visual Studio Code") >= 10:
            checks.append(self.unlock("vscode_10", self.catalog["vscode_10"]))

        if self.program_times("Visual Studio Code") >= 50:
            checks.append(self.unlock("vscode_50", self.catalog["vscode_50"]))

        if self.program_times("Steam") >= 10:
            checks.append(self.unlock("steam_10", self.catalog["steam_10"]))

        if self.program_times("Spotify") >= 10:
            checks.append(self.unlock("spotify_10", self.catalog["spotify_10"]))

        if self.program_times("TLauncher") >= 10:
            checks.append(self.unlock("tlauncher_10", self.catalog["tlauncher_10"]))

        if self.program_times("PCSX2") >= 10:
            checks.append(self.unlock("pcsx2_10", self.catalog["pcsx2_10"]))

        if self.program_times("Parsec") >= 10:
            checks.append(self.unlock("parsec_10", self.catalog["parsec_10"]))

        if total_sessions >= 1:
            checks.append(self.unlock("session_1", self.catalog["session_1"]))

        if total_sessions >= 10:
            checks.append(self.unlock("session_10", self.catalog["session_10"]))

        if total_minutes >= 60:
            checks.append(self.unlock("time_60", self.catalog["time_60"]))

        if total_minutes >= 300:
            checks.append(self.unlock("time_300", self.catalog["time_300"]))

        if bond_level >= 1:
            checks.append(self.unlock("bond_1", self.catalog["bond_1"]))

        if bond_level >= 3:
            checks.append(self.unlock("bond_3", self.catalog["bond_3"]))

        if bond_level >= 5:
            checks.append(self.unlock("bond_5", self.catalog["bond_5"]))

        return [item for item in checks if item]