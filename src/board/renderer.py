"""Board rendering primitives for Lunaris."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from src.core.engine import BoardCommand


@dataclass
class RenderedFrame:
    """Represents the result of rendering a board command."""

    description: str
    image_path: str | None = None


class ConsoleRenderer:
    """Very simple renderer that prints drawing actions to stdout."""

    def render(self, commands: Iterable[BoardCommand]) -> list[RenderedFrame]:
        frames: list[RenderedFrame] = []
        for command in commands:
            description = f"[{command.action}] {command.payload}"
            frames.append(RenderedFrame(description=description))
        return frames

