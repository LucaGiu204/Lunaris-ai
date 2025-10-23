"""User-facing session helpers for Lunaris."""

from __future__ import annotations

from dataclasses import dataclass

from src.board.renderer import ConsoleRenderer
from src.core.engine import ConversationEngine
from src.speech.synthesizer import DummySynthesizer
from src.speech.transcriber import DummyTranscriber


@dataclass
class SessionContext:
    """Bundle of components required for an interactive session."""

    engine: ConversationEngine
    renderer: ConsoleRenderer
    transcriber: DummyTranscriber
    synthesizer: DummySynthesizer


def bootstrap_session() -> SessionContext:
    """Instantiate default components for quick prototypes."""

    engine = ConversationEngine()
    renderer = ConsoleRenderer()
    transcriber = DummyTranscriber()
    synthesizer = DummySynthesizer()
    return SessionContext(
        engine=engine,
        renderer=renderer,
        transcriber=transcriber,
        synthesizer=synthesizer,
    )

