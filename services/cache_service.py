import json
from pathlib import Path


class CacheService:
    def __init__(self, cache_dir="data/cache"):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def get_path(self, key):
        safe_key = key.replace("/", "_").replace(":", "_")
        return self.cache_dir / f"{safe_key}.json"

    def get(self, key):
        path = self.get_path(key)

        if not path.exists():
            return None

        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    def set(self, key, data):
        path = self.get_path(key)

        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)