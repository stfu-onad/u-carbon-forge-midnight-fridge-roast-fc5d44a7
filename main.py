"""Midnight Fridge Roast: one line roasting a smart fridge that refuses
to open after midnight.

The program writes exactly one line to /output/entry.txt (UTF-8, a
single line of 1-200 characters including the trailing newline, per
the competition gate). Output is fully deterministic: the same fixed
line is written on every run, with no randomness, no clock reads, and
no dependence on the environment.
"""

import os

# The joke itself: exactly 130 characters, one line, no trailing spaces.
LINE = "My smart fridge locks itself after midnight, like the leftovers took out a restraining order against me."

# Gate allows at most 200 characters in the file including the newline,
# so the line itself must be at most 199 characters.
MAX_LINE_CHARS = 199

OUTPUT_PATH = "/output/entry.txt"


def validate(line: str) -> str:
    """Check the entry line against the gate before writing anything.

    Returns the line unchanged when it passes; raises ValueError
    otherwise, so a bad line can never produce a partial or invalid
    /output/entry.txt.
    """
    if not line.strip():
        raise ValueError("entry line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if not 1 <= len(line) <= MAX_LINE_CHARS:
        raise ValueError(
            f"entry line must be 1-{MAX_LINE_CHARS} chars, got {len(line)}"
        )
    return line


def main() -> None:
    line = validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
