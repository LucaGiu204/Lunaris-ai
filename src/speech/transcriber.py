"""Speech-to-text interface for Lunaris."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass
class TranscriptChunk:
    """Normalized segment returned by the transcription backend."""

    text: str
    start: float | None = None
    end: float | None = None


class TranscriptionBackend(Protocol):
    """Minimal protocol for STT providers."""

    def transcribe(self, audio_path: str) -> list[TranscriptChunk]:
        ...


class DummyTranscriber:
    """Placeholder implementation that echoes text for testing."""

    def __init__(self, fallback_text: str = "[audio pendiente]") -> None:
        self.fallback_text = fallback_text

    def transcribe(self, audio_path: str) -> list[TranscriptChunk]:
        """Return a dummy transcript while STT is integrated."""

        return [TranscriptChunk(text=self.fallback_text)]

