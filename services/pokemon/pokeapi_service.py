from services.api_client import ApiClient
from services.pokemon.form_translator import FormTranslator
from services.pokemon.asuka_dex import AsukaDex
from services.pokemon.pokemon_scan_text import PokemonScanText


class PokeApiService:
    def __init__(self):
        self.client = ApiClient()
        self.form_translator = FormTranslator()
        self.asuka_dex = AsukaDex()
        self.scan_text = PokemonScanText()
        self.base_url = "https://pokeapi.co/api/v2"

    def resolve_name(self, name):
        translated = self.form_translator.translate(name)

        dex_entry = self.asuka_dex.find(translated)

        if dex_entry:
            return dex_entry["api_name"]

        return translated

    def format_dex_entry(self, entry):
        pokemon = {
            "name": entry["api_name"],
            "id": entry.get("id"),
            "height": entry.get("height"),
            "weight": entry.get("weight"),
            "types": entry.get("types", []),
            "abilities": [
                ability["name"] if isinstance(ability, dict) else ability
                for ability in entry.get("abilities", [])
            ],
            "stats": entry.get("stats", {})
        }

        pokemon["scan_text"] = self.scan_text.generate(pokemon)

        return pokemon

    def get_pokemon(self, name):
        resolved_name = self.resolve_name(name)

        dex_entry = self.asuka_dex.find(resolved_name)

        if dex_entry and "stats" in dex_entry:
            print(f"[ASUKADEX] Encontrado localmente: {resolved_name}")
            return self.format_dex_entry(dex_entry)

        print(f"[POKEAPI] Consultando online: {resolved_name}")

        url = f"{self.base_url}/pokemon/{resolved_name}"
        cache_key = f"pokemon_{resolved_name}"

        data = self.client.get_json(url, cache_key)

        if not data:
            return None

        pokemon = {
            "name": data["name"],
            "id": data["id"],
            "height": data["height"],
            "weight": data["weight"],
            "types": [
                item["type"]["name"]
                for item in data["types"]
            ],
            "abilities": [
                item["ability"]["name"]
                for item in data["abilities"]
            ],
            "stats": {
                item["stat"]["name"]: item["base_stat"]
                for item in data["stats"]
            }
        }

        pokemon["scan_text"] = self.scan_text.generate(pokemon)

        return pokemon