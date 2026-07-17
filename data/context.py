from data.habits import HabitEngine
from data.daily import DailyEngine
from data.achievements import AchievementEngine


class ContextEngine:
    def __init__(self):
        self.habits = HabitEngine()
        self.daily = DailyEngine()
        self.achievements = AchievementEngine()

    def startup_messages(self):
        messages = []

        daily_message = self.daily.daily_message()
        habit_message = self.habits.habit_message()

        if daily_message:
            messages.append(daily_message)

        if habit_message:
            messages.append(habit_message)

        return messages

    def after_command_messages(self):
        return self.achievements.check()