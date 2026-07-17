import time


class VoiceState:
    def __init__(self):
        self.state = "text"
        self.last_interaction = time.time()
        self.conversation_timeout = 20

    def set_text_mode(self):
        self.state = "text"

    def set_idle(self):
        self.state = "idle"

    def set_listening(self):
        self.state = "listening"

    def set_conversation(self):
        self.state = "conversation"
        self.last_interaction = time.time()

    def refresh_conversation(self):
        self.last_interaction = time.time()

    def conversation_expired(self):
        return time.time() - self.last_interaction > self.conversation_timeout

    def is_text(self):
        return self.state == "text"

    def is_idle(self):
        return self.state == "idle"

    def is_conversation(self):
        return self.state == "conversation"