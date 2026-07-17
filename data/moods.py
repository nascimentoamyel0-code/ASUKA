import json
import os
import random
from datetime import datetime

from moods.calm import CalmMood
from moods.cheerful import CheerfulMood
from moods.curious import CuriousMood
from moods.playful import PlayfulMood
from moods.sleepy import SleepyMood


class MoodEngine:
    def __init__(self):
        self.moods_file = "data/moods.json"

        self.available_moods = {
            "calm": CalmMood(),
            "cheerful": CheerfulMood(),
            "curious": CuriousMood(),
            "playful": PlayfulMood(),
            "sleepy": SleepyMood()
        }

        self.current_mood_name = self.load_current_mood()

    def load_current_mood(self):
        if not os.path.exists(self.moods_file):
            self.save_current_mood("calm")
            return "calm"

        try:
            with open(self.moods_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                return data.get("current_mood", "calm")
        except Exception:
            return "calm"

    def save_current_mood(self, mood_name):
        data = {"current_mood": mood_name}

        with open(self.moods_file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def get_current_mood(self):
        return self.available_moods.get(
            self.current_mood_name,
            self.available_moods["calm"]
        )

    def set_mood(self, mood_name):
        mood_name = mood_name.lower()

        if mood_name not in self.available_moods:
            return False

        self.current_mood_name = mood_name
        self.save_current_mood(mood_name)
        return True

    def random_mood(self):
        mood = random.choice(list(self.available_moods.keys()))
        self.set_mood(mood)
        return mood

    def auto_mood(self):
        hour = datetime.now().hour

        if 6 <= hour < 12:
            self.set_mood("cheerful")
        elif 12 <= hour < 18:
            self.set_mood("curious")
        elif 18 <= hour < 23:
            self.set_mood("playful")
        else:
            self.set_mood("sleepy")

        return self.current_mood_name