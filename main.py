#!/usr/bin/env python3
"""Seventeen Syllables of Debugging.

Writes one original haiku about debugging (5-7-5 syllables, 17 total)
to /output/entry.txt and asserts the competition gate before writing:
exactly three lines, 5-7-5 syllables, 1-200 characters, not blank.
"""

import os

HAIKU = (
    "Still the cursor blinks\n"
    "log says nothing's wrong \u2014 again\n"
    "the bug just waves back\n"
)

# Syllable count per word, counted by hand for the exact words used.
SYLLABLES = {
    "still": 1, "the": 1, "cursor": 2, "blinks": 1,
    "log": 1, "says": 1, "nothing's": 2, "wrong": 1, "again": 2,
    "bug": 1, "just": 1, "waves": 1, "back": 1,
}

EXPECTED = (5, 7, 5)


def count_syllables(line):
    words = line.replace("\u2014", " ").split()
    return sum(SYLLABLES[word.lower()] for word in words)


def main():
    lines = HAIKU.splitlines()
    assert len(lines) == 3, f"haiku must have 3 lines, got {len(lines)}"
    for line, expected in zip(lines, EXPECTED):
        got = count_syllables(line)
        assert got == expected, f"{line!r}: {got} syllables, expected {expected}"
    total = sum(EXPECTED)
    assert total == 17, f"haiku must total 17 syllables, got {total}"
    assert 1 <= len(HAIKU) <= 200, f"entry must be 1-200 chars, got {len(HAIKU)}"
    assert HAIKU.strip(), "entry must not be only whitespace"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
