from core.normalizer import Normalizer

normalizer = Normalizer()

while True:
    text = input("Você: ")
    print("Normalizado:", normalizer.normalize(text))
    