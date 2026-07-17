import json
import os
from datetime import datetime


class AdaptiveEngine:
    def __init__(self):
        self.memory_file = "data/path_memory.json"

    def load_memory(self):
        if not os.path.exists(self.memory_file):
            return {"repairs": []}

        with open(self.memory_file, "r", encoding="utf-8") as file:
            return json.load(file)

    def save_memory(self, data):
        with open(self.memory_file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def remember_repair(self, program_name, old_path, new_path):
        data = self.load_memory()

        data["repairs"].append({
            "program": program_name,
            "old_path": old_path,
            "new_path": new_path,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        self.save_memory(data)

    def scan_drive(self, drive, exe_name):
        drive = drive.upper().replace(":", "")
        root = f"{drive}:/"

        if not os.path.exists(root):
            return []

        results = []

        for current_path, folders, files in os.walk(root):
            for file in files:
                if file.lower() == exe_name.lower():
                    full_path = os.path.join(current_path, file)
                    results.append(full_path.replace("\\", "/"))

        return results

    def find_exe(self, drives, exe_name):
        for drive in drives:
            results = self.scan_drive(drive, exe_name)

            if results:
                return results

        return []