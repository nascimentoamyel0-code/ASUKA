from core.intent_matcher import IntentMatcher

matcher = IntentMatcher()

while True:

    text = input("Você: ")

    intent, score = matcher.match(text)

    print(intent)
    print(score)
    print("-" * 40)