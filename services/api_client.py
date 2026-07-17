import requests

from services.cache_service import CacheService


class ApiClient:
    def __init__(self):
        self.cache = CacheService()

    def get_json(self, url, cache_key=None, use_cache=True):
        if use_cache and cache_key:
            cached = self.cache.get(cache_key)

            if cached:
                return cached

        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return None

        data = response.json()

        if use_cache and cache_key:
            self.cache.set(cache_key, data)

        return data