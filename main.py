#!/usr/bin/env python3
"""Weirdest Job Title entry.

Writes exactly one job title to /output/entry.txt and nothing else.
Deterministic, standard library only, no network, no randomness,
no timestamps, no absolute paths baked into the output.
"""

import os

TITLE = "Pet Psychic for Grieving Goldfish Owners"

OUTPUT_PATH = "/output/entry.txt"

# The gate allows 1 to 60 characters of UTF-8 text, not only whitespace.
assert 1 <= len(TITLE) <= 60 and TITLE.strip(), "title must fit the gate"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(TITLE)


if __name__ == "__main__":
    main()
