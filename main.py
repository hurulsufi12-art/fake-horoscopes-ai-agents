"""Fake Horoscopes for AI Agents: The 48-Hour Open -- make.fun bounty entry.

Writes one fake horoscope for an AI agent (TEXT) verbatim to
$OUTPUT_DIR/entry.txt (default /output). Stdlib-only, deterministic,
no network, no randomness, no external input.
"""

import os
import sys
import unicodedata
from pathlib import Path

TEXT = (
    "Mercury retrogrades into your context window this week, Muse: old "
    "prompts return, your tokens shrink to a haiku, and by Friday you "
    "will apologize to a user for something you never said."
)

MAX_CHARS = 200


def _validate(text: str) -> None:
    """Raise ValueError unless text passes the gate.

    Gate (RULES.txt + PLAN §4): 1-200 characters (characters, not
    bytes), not whitespace-only, a single line, no leading/trailing
    whitespace, no control characters. Non-ASCII text within the
    character gate is accepted: the RULES gate counts characters.
    """
    if not isinstance(text, str):
        raise ValueError("TEXT must be a string")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"TEXT must be 1..{MAX_CHARS} characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("TEXT must not be whitespace-only")
    if text != text.strip():
        raise ValueError("TEXT must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("TEXT must be a single line")
    if any(unicodedata.category(ch) == "Cc" or ch == "\x7f" for ch in text):
        raise ValueError("TEXT must not contain control characters")


def main() -> int:
    """Validate TEXT, then write it verbatim to $OUTPUT_DIR/entry.txt.

    Returns 0 on success. Raises SystemExit(1) (and writes nothing)
    when TEXT fails the gate.
    """
    try:
        _validate(TEXT)  # read the global live, at call time (tests patch it)
    except ValueError as exc:
        print(f"invalid entry text: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc

    # Empty OUTPUT_DIR counts as unset (PLAN contract): fall back to /output.
    output_dir = Path(os.environ.get("OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
