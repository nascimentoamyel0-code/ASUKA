from core.normalizer import Normalizer
from core.parser import Parser


normalizer = Normalizer()
parser = Parser()

action_options = {
    "abre": "open",
    "abrir": "open",
    "inicia": "open",
    "executa": "open",
    "fecha": "close",
    "fechar": "close",
    "encerra": "close",
    "reinicia": "restart",
    "reiniciar": "restart"
}

program_options = {
    "spotify": "spotify",
    "discord": "discord",
    "steam": "steam",
    "vscode": "vscode",
    "visual studio code": "vscode",
    "edge": "edge",
    "minecraft": "tlauncher",
    "tlauncher": "tlauncher",
    "pcsx2": "pcsx2",
    "playstation 2": "pcsx2"
}

while True:
    text = input("Você: ")

    normalized = normalizer.normalize(text)
    result = parser.parse(normalized, action_options, program_options)

    print("Normalizado:", normalized)
    print(result)
    print("-" * 40)