import json
from pathlib import Path


class AsukaDex:
    def __init__(self):
        self.dex_path = Path("data/pokemon/pokemon_dex.json")
        self.registry_path = Path("data/pokemon/pokemon_registry.json")

    def load_json(self, path):
        if not path.exists():
            return {}

        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    def load_dex(self):
        return self.load_json(self.dex_path)

    def load_registry(self):
        return self.load_json(self.registry_path)

    def find_in_data(self, name, data):
        name = name.lower().strip().replace("_", "-")

        if name in data:
            return data[name]

        readable_name = name.replace("-", " ")

        for _, entry in data.items():
            aliases = entry.get("aliases", [])

            if name in aliases or readable_name in aliases:
                return entry

        return None

    def find(self, name):
        dex = self.load_dex()

        result = self.find_in_data(name, dex)

        if result:
            return result

        registry = self.load_registry()

        return self.find_in_data(name, registry)