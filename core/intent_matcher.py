from rapidfuzz import process, fuzz


class IntentMatcher:

    def __init__(self):

        self.commands = {

            "OPEN_SPOTIFY": [
                "spotify",
                "abre spotify",
                "abrir spotify",
                "inicia spotify",
                "executa spotify",
                "quero ouvir musica",
                "musica"
            ],

            "OPEN_DISCORD": [
                "discord",
                "abre discord",
                "abrir discord",
                "inicia discord",
                "executa discord"
            ],

            "OPEN_STEAM": [
                "steam",
                "abre steam",
                "abrir steam",
                "executa steam"
            ],

            "OPEN_VSCODE": [
                "vscode",
                "visual studio code",
                "abre vscode",
                "abre visual studio",
                "editor de codigo"
            ],

            "OPEN_EDGE": [
                "edge",
                "microsoft edge",
                "abre edge",
                "abrir navegador",
                "abre navegador"
            ],

            "OPEN_TLAUNCHER": [
                "minecraft",
                "tlauncher",
                "abre minecraft",
                "abre tlauncher",
                "jogar minecraft"
            ],

            "OPEN_PCSX2": [
                "pcsx2",
                "playstation 2",
                "abre pcsx2",
                "abrir ps2",
                "emulador ps2"
            ]

        }

        self.all_phrases = {}

        for intent, phrases in self.commands.items():

            for phrase in phrases:

                self.all_phrases[phrase] = intent

    def match(self, text):

        result = process.extractOne(
            text.lower(),
            self.all_phrases.keys(),
            scorer=fuzz.WRatio
        )

        if result is None:
            return None, 0

        phrase, score, _ = result

        intent = self.all_phrases[phrase]

        return intent, score