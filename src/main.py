"""Entry point for early Lunaris experiments."""

from __future__ import annotations

from src.interface.session import bootstrap_session


def demo_run() -> None:
    """Execute a minimal round-trip using the placeholder components."""

    context = bootstrap_session()
    transcript = "Explicame qué es una derivada."
    context.engine.ingest_transcript(transcript)
    reply = context.engine.generate_response()

    frames = context.renderer.render(context.engine.pending_board_commands())

    print("Usuario:", transcript)
    print("Asistente:", reply.text)
    if frames:
        print("Comandos de pizarra:")
        for frame in frames:
            print(" -", frame.description)
    else:
        print("(Sin comandos de pizarra por ahora)")


if __name__ == "__main__":
    demo_run()

