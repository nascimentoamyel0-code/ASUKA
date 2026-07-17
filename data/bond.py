import json
import os


class BondEngine:
    def __init__(self):
        self.file_path = "data/bond.json"
        self.data = self.load_bond()

    def load_bond(self):
        if not os.path.exists(self.file_path):
            data = {"points": 0, "level": 0}
            self.save_bond(data)
            return data

        with open(self.file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def save_bond(self, data=None):
        if data is None:
            data = self.data

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def add_points(self, amount=1):
        self.data["points"] += amount
        self.data["level"] = self.calculate_level()
        self.save_bond()

    def calculate_level(self):
        points = self.data["points"]

        if points >= 500:
            return 5
        if points >= 250:
            return 4
        if points >= 100:
            return 3
        if points >= 50:
            return 2
        if points >= 10:
            return 1

        return 0

    def get_level(self):
        return self.data["level"]

    def get_points(self):
        return self.data["points"]

    def bond_message(self):
        level = self.get_level()

        if level >= 5:
            return "Já passamos bastante tempo juntos. Vamos continuar de onde paramos?"
        if level >= 4:
            return "Bem-vindo de volta. Eu estava pronta para continuar."
        if level >= 3:
            return "Oi de novo. Bom te ver por aqui."
        if level >= 2:
            return "Estamos evoluindo bem juntos."
        if level >= 1:
            return "Acho que estou começando a me acostumar com você."

        return None