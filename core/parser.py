from rapidfuzz import process, fuzz


class Parser:
    def __init__(self):
        self.min_score = 72

    def fuzzy_match(self, text, options):
        if not text or not options:
            return None, 0, None

        result = process.extractOne(
            text,
            options.keys(),
            scorer=fuzz.WRatio
        )

        if not result:
            return None, 0, None

        phrase, score, _ = result

        if score < self.min_score:
            return None, score, phrase

        return options[phrase], score, phrase

    def parse_action(self, command, action_options):
        words = command.split()

        if not words:
            return None, 0, None

        possible_action = words[0]

        action, score, phrase = self.fuzzy_match(
            possible_action,
            action_options
        )

        return action, score, phrase

    def parse_target(self, command, program_options):
        words = command.split()

        if len(words) <= 1:
            possible_target = command
        else:
            possible_target = " ".join(words[1:])

        target, score, phrase = self.fuzzy_match(
            possible_target,
            program_options
        )

        return target, score, phrase

    def parse(self, command, action_options, program_options):
        action, action_score, action_phrase = self.parse_action(
            command,
            action_options
        )

        target, target_score, target_phrase = self.parse_target(
            command,
            program_options
        )

        return {
            "action": action,
            "target": target,
            "confidence": min(action_score, target_score),
            "debug": {
                "action_phrase": action_phrase,
                "action_score": action_score,
                "target_phrase": target_phrase,
                "target_score": target_score
            }
        }