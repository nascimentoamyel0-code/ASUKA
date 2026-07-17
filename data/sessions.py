import json
import os
from datetime import datetime


class SessionEngine:
    def __init__(self):
        self.file_path = "data/sessions.json"
        self.start_time = datetime.now()
        self.data = self.load_sessions()

    def load_sessions(self):
        if not os.path.exists(self.file_path):
            default_data = {
                "total_sessions": 0,
                "total_minutes": 0,
                "last_session": None
            }
            self.save_sessions(default_data)
            return default_data

        with open(self.file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def save_sessions(self, data=None):
        if data is None:
            data = self.data

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def end_session(self):
        end_time = datetime.now()
        duration = end_time - self.start_time
        minutes = int(duration.total_seconds() // 60)

        self.data["total_sessions"] += 1
        self.data["total_minutes"] += minutes
        self.data["last_session"] = {
            "started_at": self.start_time.strftime("%Y-%m-%d %H:%M:%S"),
            "ended_at": end_time.strftime("%Y-%m-%d %H:%M:%S"),
            "duration_minutes": minutes
        }

        self.save_sessions()

        return minutes

    def get_total_minutes(self):
        return self.data["total_minutes"]

    def get_total_sessions(self):
        return self.data["total_sessions"]