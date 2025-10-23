"""Text-to-speech placeholder for Lunaris."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class SpeechOutput:
    """Represents a synthesized audio clip."""

    audio_path: str
    text: str


class DummySynthesizer:
    """Return static audio references until a real TTS is integrated."""

    def __init__(self, cache_dir: str = "./tmp/tts") -> None:
        self.cache_dir = cache_dir

    def synthesize(self, text: str) -> SpeechOutput:
        """Produce a dummy audio artifact path.

        A proper implementation will call `pyttsx3` or an API provider and save
        the resulting waveform. Keeping the structure ready simplifies future
        integration.
        """

        fake_path = f"{self.cache_dir}/placeholder.wav"
        return SpeechOutput(audio_path=fake_path, text=text)

