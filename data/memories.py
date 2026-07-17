import json
import os
from datetime import datetime


class MemoryEngine:
    def __init__(self):
        self.memories_file = "data/memories.json"
        self.memories = self.load_memories()

    def load_memories(self):
        if not os.path.exists(self.memories_file):
            default_data = {
                "created_at": "2026-06-30",
                "program_usage": {},
                "last_program_opened": None,
                "total_commands": 0
            }

            self.save_memories(default_data)
            return default_data

        try:
            with open(self.memories_file, "r", encoding="utf-8") as file:
                return json.load(file)
        except Exception:
            return {
                "created_at": "2026-06-30",
                "program_usage": {},
                "last_program_opened": None,
                "total_commands": 0
            }

    def save_memories(self, data=None):
        if data is None:
            data = self.memories

        with open(self.memories_file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def register_command(self):
        self.memories["total_commands"] += 1
        self.save_memories()

    def register_program_opened(self, program_name):
        self.memories["last_program_opened"] = program_name

        usage = self.memories["program_usage"]

        if program_name not in usage:
            usage[program_name] = {
                "times_opened": 0,
                "last_opened": None
            }

        usage[program_name]["times_opened"] += 1
        usage[program_name]["last_opened"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.save_memories()

    def get_program_usage(self, program_name):
        return self.memories["program_usage"].get(program_name)

    def get_total_commands(self):
        return self.memories["total_commands"]

    def get_last_program_opened(self):
        return self.memories["last_program_opened"]