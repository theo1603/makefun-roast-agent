#!/usr/bin/env python3
"""Roast Your Own Agent — write one roast line to /output/entry.txt.

One line, at most 200 characters, roasting my own AI agent: it treats a
tiny mint ceiling like scripture, then burns hours of compute hunting a
free NFT worth almost nothing. Playful and self-deprecating, never
hateful — the joke is aimed at my own agent, not at any person.
"""

import os

ENTRY = (
    "My agent treats a Rp1,000 mint ceiling like scripture, then burns "
    "three hours of compute hunting a free NFT worth Rp273."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
