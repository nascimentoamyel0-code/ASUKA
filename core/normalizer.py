import unicodedata
import re


class Normalizer:
    def __init__(self):
        self.noise_words = [
            "o", "a", "os", "as",
            "um", "uma", "uns", "umas",
            "por favor", "pfv", "pls",
            "pra", "para",
            "da", "de", "do", "das", "dos",
            "meu", "minha",
            "asuka"
        ]

    def remove_accents(self, text):
        normalized = unicodedata.normalize("NFD", text)

        return "".join(
            char for char in normalized
            if unicodedata.category(char) != "Mn"
        )

    def normalize(self, text):
        if not text:
            return ""

        text = text.lower().strip()
        text = self.remove_accents(text)

        text = re.sub(r"[^\w\s]", " ", text)
        text = re.sub(r"\s+", " ", text).strip()

        for word in self.noise_words:
            text = re.sub(rf"\b{word}\b", " ", text)

        text = re.sub(r"\s+", " ", text).strip()

        return text