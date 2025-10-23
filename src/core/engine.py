"""Core orchestration logic for Lunaris.

This module centralises the conversation flow between the speech, language
model and board subsystems. The real implementation will:

- Maintain the dialogue state of the tutoring session.
- Delegate speech-to-text transcription requests to :mod:`speech.transcriber`.
- Invoke the reasoning model (LLM) to generate explanations and drawing
  commands.
- Forward drawing instructions to :mod:`board.renderer` and audio prompts to
  :mod:`speech.synthesizer`.

The current skeleton defines the public interface that other modules can target
while the implementation is developed iteratively.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass
class BoardCommand:
    """Structured command that the board renderer can consume."""

    action: str
    payload: dict


@dataclass
class Utterance:
    """Represents a message exchanged during the tutoring session."""

    speaker: str
    text: str


@dataclass
class SessionState:
    """In-memory representation of the ongoing tutoring session."""

    history: List[Utterance] = field(default_factory=list)
    board_commands: List[BoardCommand] = field(default_factory=list)


class ConversationEngine:
    """High-level coordinator for Lunaris interactions."""

    def __init__(self) -> None:
        self.state = SessionState()

    def ingest_transcript(self, text: str) -> None:
        """Store a user transcript and trigger the reasoning pipeline.

        The method is intentionally left as a stub so that future iterations can
        connect to the speech-to-text module and the LLM backend.
        """

        self.state.history.append(Utterance(speaker="user", text=text))

    def generate_response(self) -> Utterance:
        """Return a placeholder assistant response.

        The real version will call the LLM and populate :class:`BoardCommand`
        objects. For now we keep the behaviour deterministic for early tests.
        """

        reply = Utterance(
            speaker="assistant",
            text=(
                "Este es un stub de respuesta. Implementa la llamada al LLM "
                "para generar explicaciones personalizadas."
            ),
        )
        self.state.history.append(reply)
        return reply

    def pending_board_commands(self) -> List[BoardCommand]:
        """Expose commands generated during the last reasoning cycle."""

        return list(self.state.board_commands)

