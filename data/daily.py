import json
import os
from datetime import datetime


class DailyEngine:
    def __init__(self):
        self.file_path = "data/daily.json"
        self.data = self.load()

    def load(self):
        if not os.path.exists(self.file_path):
            data = {
                "last_seen": None,
                "days_used": 0
            }
            self.save(data)
            return data

        with open(self.file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def save(self, data=None):
        if data is None:
            data = self.data

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def check_today(self):
        today = datetime.now().strftime("%Y-%m-%d")
        last_seen = self.data.get("last_seen")

        if last_seen != today:
            self.data["last_seen"] = today
            self.data["days_used"] += 1
            self.save()
            return True

        return False

    def get_days_used(self):
        return self.data["days_used"]

    def daily_message(self):
        is_new_day = self.check_today()

        if is_new_day:
            return f"Hoje é o dia {self.get_days_used()} usando a Asuka."

        return None