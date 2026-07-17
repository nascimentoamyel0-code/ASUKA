import json
from pathlib import Path

from services.api_client import ApiClient


class PokemonDexBuilder:
    def __init__(self):
        self.client = ApiClient()
        self.base_url = "https://pokeapi.co/api/v2"

        self.data_dir = Path("data/pokemon")
        self.registry_path = self.data_dir / "pokemon_registry.json"
        self.dex_path = self.data_dir / "pokemon_dex.json"

    def load_registry(self):
        if not self.registry_path.exists():
            print("Registro não encontrado. Rode sync_pokemon_registry.py primeiro.")
            return {}

        with open(self.registry_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def get_pokemon_data(self, api_name):
        url = f"{self.base_url}/pokemon/{api_name}"
        return self.client.get_json(url, f"pokemon_{api_name}")

    def build_entry(self, api_name, registry_data):
        data = self.get_pokemon_data(api_name)

        if not data:
            return None

        return {
            "api_name": api_name,
            "display_name": registry_data.get(
                "display_name",
                api_name.replace("-", " ").title()
            ),
            "kind": registry_data.get("kind", "pokemon"),
            "aliases": registry_data.get("aliases", []),

            "id": data.get("id"),
            "height": data.get("height"),
            "weight": data.get("weight"),

            "types": [
                item["type"]["name"]
                for item in data.get("types", [])
            ],

            "abilities": [
                {
                    "name": item["ability"]["name"],
                    "hidden": item["is_hidden"]
                }
                for item in data.get("abilities", [])
            ],

            "stats": {
                item["stat"]["name"]: item["base_stat"]
                for item in data.get("stats", [])
            },

            "forms": [
                form["name"]
                for form in data.get("forms", [])
            ],

            "sprites": {
                "front_default": data.get("sprites", {}).get("front_default"),
                "official_artwork": (
                    data.get("sprites", {})
                    .get("other", {})
                    .get("official-artwork", {})
                    .get("front_default")
                )
            }
        }

    def build(self, limit=None):
        registry = self.load_registry()

        if not registry:
            return False

        dex = {}

        items = list(registry.items())

        if limit:
            items = items[:limit]

        total = len(items)

        for index, (api_name, registry_data) in enumerate(items, start=1):
            print(f"[{index}/{total}] Baixando {api_name}...")

            entry = self.build_entry(api_name, registry_data)

            if entry:
                dex[api_name] = entry

        with open(self.dex_path, "w", encoding="utf-8") as file:
            json.dump(dex, file, indent=4, ensure_ascii=False)

        print(f"\nAsukaDex salva em: {self.dex_path}")
        print(f"Total na Dex: {len(dex)}")

        return True