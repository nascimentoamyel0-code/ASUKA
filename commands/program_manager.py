import json
import os
import subprocess
import time
from pathlib import Path

import pygetwindow as gw

from core.adaptive.adaptive_engine import AdaptiveEngine


class ProgramManager:
    def __init__(self):
        self.plugins_path = Path("plugins/programs")
        self.programs = self.load_plugins()
        self.adaptive = AdaptiveEngine()

    def load_plugins(self):
        programs = {}

        if not self.plugins_path.exists():
            self.plugins_path.mkdir(parents=True, exist_ok=True)

        for file in self.plugins_path.glob("*.json"):
            with open(file, "r", encoding="utf-8") as f:
                data = json.load(f)

            program_id = data.get("id", file.stem).upper()
            programs[program_id] = data

        return programs

    def save_plugin(self, program):
        data = self.get_program_data(program)

        if not data:
            return False

        file_path = self.plugins_path / f"{program.lower()}.json"

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        return True

    def get_program_data(self, program):
        if not program:
            return None

        return self.programs.get(program.upper())

    def extract_exe_path(self, path):
        path = os.path.expandvars(path)
        lower_path = path.lower()

        if ".exe" in lower_path:
            index = lower_path.find(".exe") + 4
            return path[:index]

        return path

    def update_program_path(self, program, new_path):
        program_key = program.upper()

        if program_key not in self.programs:
            return False

        old_path = self.programs[program_key]["path"]

        self.programs[program_key]["path"] = new_path.replace("\\", "/")
        self.save_plugin(program_key)

        self.adaptive.remember_repair(
            self.programs[program_key]["name"],
            old_path,
            new_path
        )

        return True

    def is_running(self, program):
        data = self.get_program_data(program)

        if not data:
            return False

        process_name = data.get("process")

        if not process_name:
            return False

        result = subprocess.run(
            ["tasklist", "/FI", f"IMAGENAME eq {process_name}"],
            capture_output=True,
            text=True
        )

        return process_name.lower() in result.stdout.lower()

    def focus_window(self, program):
        data = self.get_program_data(program)

        if not data:
            return False

        possible_titles = [
            data.get("window_title"),
            data.get("name"),
            program
        ]

        possible_titles = [
            title.lower()
            for title in possible_titles
            if title
        ]

        try:
            windows = gw.getAllWindows()

            for window in windows:
                title = window.title.lower()

                if any(possible in title for possible in possible_titles):
                    if window.isMinimized:
                        window.restore()

                    window.activate()
                    return True

        except Exception:
            return False

        return False

    def repair_path(self, program, drives):
        data = self.get_program_data(program)

        if not data:
            return {
                "success": False,
                "reason": "program_not_found",
                "matches": []
            }

        exe_name = data.get("process")

        if not exe_name:
            exe_path = self.extract_exe_path(data["path"])
            exe_name = os.path.basename(exe_path)

        matches = self.adaptive.find_exe(drives, exe_name)

        if not matches:
            return {
                "success": False,
                "reason": "not_found",
                "matches": []
            }

        chosen_path = matches[0]

        self.update_program_path(program, chosen_path)

        return {
            "success": True,
            "new_path": chosen_path,
            "matches": matches
        }

    def open(self, program):
        data = self.get_program_data(program)

        if not data:
            return {
                "success": False,
                "name": program,
                "reason": "not_found"
            }

        name = data["name"]
        path = os.path.expandvars(data["path"])
        exe_path = self.extract_exe_path(path)

        if not os.path.exists(exe_path):
            return {
                "success": False,
                "name": name,
                "reason": "path_not_found",
                "exe_name": data.get("process") or os.path.basename(exe_path)
            }

        if self.is_running(program):
            focused = self.focus_window(program)

            return {
                "success": True,
                "name": name,
                "already_running": True,
                "focused": focused
            }

        try:
            subprocess.Popen(f'"{path}"', shell=True)

            time.sleep(1)

            focused = self.focus_window(program)

            return {
                "success": True,
                "name": name,
                "already_running": False,
                "focused": focused
            }

        except Exception as error:
            return {
                "success": False,
                "name": name,
                "reason": "open_error",
                "message": str(error)
            }

    def close(self, program):
        data = self.get_program_data(program)

        if not data:
            return {
                "success": False,
                "name": program
            }

        name = data["name"]
        process_name = data.get("process")

        if not process_name:
            return {
                "success": False,
                "name": name
            }

        if not self.is_running(program):
            return {
                "success": True,
                "name": name,
                "already_closed": True
            }

        subprocess.run(
            ["taskkill", "/IM", process_name, "/F"],
            capture_output=True,
            text=True
        )

        return {
            "success": True,
            "name": name,
            "already_closed": False
        }

    def restart(self, program):
        data = self.get_program_data(program)

        if not data:
            return {
                "success": False,
                "name": program
            }

        name = data["name"]

        self.close(program)

        time.sleep(data.get("restart_delay", 1))

        result = self.open(program)

        if result["success"]:
            return {
                "success": True,
                "name": name
            }

        return {
            "success": False,
            "name": name
        }