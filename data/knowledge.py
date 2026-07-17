import json
import os


class KnowledgeEngine:
    def __init__(self):
        self.file_path = "data/knowledge.json"
        self.data = self.load()

    def load(self):
        if not os.path.exists(self.file_path):
            data = {"facts": {}}
            self.save(data)
            return data

        with open(self.file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def save(self, data=None):
        if data is None:
            data = self.data

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def remember(self, key, value):
        self.data["facts"][key] = value
        self.save()

    def recall(self, key):
        return self.data["facts"].get(key)

    def list_facts(self):
        return self.data["facts"]