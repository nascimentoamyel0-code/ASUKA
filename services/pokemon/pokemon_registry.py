import json
from pathlib import Path

from services.api_client import ApiClient


class PokemonRegistry:
    def __init__(self):
        self.client = ApiClient()
        self.base_url = "https://pokeapi.co/api/v2"

        self.data_dir = Path("data/pokemon")
        self.data_dir.mkdir(parents=True, exist_ok=True)

        self.registry_path = self.data_dir / "pokemon_registry.json"

    def get_all(self, endpoint):
        url = f"{self.base_url}/{endpoint}?limit=20000"
        return self.client.get_json(
            url,
            cache_key=f"{endpoint}_all_list",
            use_cache=False
        )

    def sync(self):
        print("Baixando Pokémon...")
        pokemon_data = self.get_all("pokemon")

        print("Baixando formas Pokémon...")
        form_data = self.get_all("pokemon-form")

        if not pokemon_data or not form_data:
            print("Erro ao baixar dados da PokéAPI.")
            return False

        registry = {}

        for item in pokemon_data["results"]:
            name = item["name"]

            registry[name] = {
                "api_name": name,
                "kind": "pokemon",
                "display_name": name.replace("-", " ").title(),
                "aliases": [
                    name,
                    name.replace("-", " ")
                ]
            }

        for item in form_data["results"]:
            name = item["name"]

            if name not in registry:
                registry[name] = {
                    "api_name": name,
                    "kind": "pokemon-form",
                    "display_name": name.replace("-", " ").title(),
                    "aliases": [
                        name,
                        name.replace("-", " ")
                    ]
                }
            else:
                registry[name]["kind"] = "pokemon-and-form"

        with open(self.registry_path, "w", encoding="utf-8") as file:
            json.dump(registry, file, indent=4, ensure_ascii=False)

        print(f"Registro salvo em: {self.registry_path}")
        print(f"Total registrado: {len(registry)} Pokémon/formas")

        return True

    def load(self):
        if not self.registry_path.exists():
            return {}

        with open(self.registry_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def find(self, name):
        name = name.lower().strip().replace("_", "-")
        registry = self.load()

        if name in registry:
            return registry[name]

        readable_name = name.replace("-", " ")

        for _, data in registry.items():
            if readable_name in data["aliases"]:
                return data

        return None