"""Midnight Fridge Roast: one line roasting a smart fridge that refuses
to open after midnight.

Writes the line to /output/entry.txt (UTF-8, single line, 1-200 chars
including the trailing newline, per the gate).
"""

import os

LINE = "My smart fridge locks itself after midnight, like the leftovers took out a restraining order against me."

MAX_CHARS = 199  # plus one trailing newline keeps the file at <= 200 chars


def main() -> None:
    # Validate the line before writing anything, so a bad line never
    # produces a partial or invalid /output/entry.txt.
    line = LINE
    if not line.strip():
        raise ValueError("entry line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"entry line must be 1-{MAX_CHARS} chars, got {len(line)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
