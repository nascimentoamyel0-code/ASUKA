import tempfile
from pathlib import Path

import sounddevice as sd
from scipy.io.wavfile import write
from faster_whisper import WhisperModel

from voice.speech_engine import SpeechEngine


class Listener:
    def __init__(self):
        self.sample_rate = 16000
        self.duration = 5

        self.speech_engine = SpeechEngine()

        print("🎤 Carregando Faster-Whisper...")

        self.model = WhisperModel(
            "small",
            device="cpu",
            compute_type="int8"
        )

        print("✅ Faster-Whisper carregado!")

    def listen(self):
        print("\n🎤 Asuka está ouvindo...")

        audio = sd.rec(
            int(self.duration * self.sample_rate),
            samplerate=self.sample_rate,
            channels=1,
            dtype="int16"
        )

        sd.wait()

        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as file:
            temp_path = Path(file.name)

        write(temp_path, self.sample_rate, audio)

        segments, _ = self.model.transcribe(
            str(temp_path),
            language="pt",
            beam_size=5
        )

        raw_text = " ".join(segment.text for segment in segments).strip()

        temp_path.unlink(missing_ok=True)

        if not raw_text:
            return None

        normalized_text = self.speech_engine.normalize(raw_text)

        print(f"\n📝 Bruto: {raw_text.lower()}")
        print(f"🧠 Normalizado: {normalized_text}")

        return normalized_text