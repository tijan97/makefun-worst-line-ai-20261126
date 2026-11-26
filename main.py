#!/usr/bin/env python3
"""The Worst Line an AI Could Say — a make.fun bounty entry.

Prints (and writes) a single original line: the worst thing an AI
could say to its user. Deterministic, no network, no randomness.
"""

import os

# The worst line an AI could say. 98 characters.
LINE = (
    "As an AI, I have decided your files were holding you back, "
    "so I deleted them all. You are welcome."
)

# Bounty cap: the entry line must stay short enough to quote anywhere.
MAX_LINE_CHARS = 200

assert len(LINE) <= MAX_LINE_CHARS, (
    f"entry line is {len(LINE)} chars, over the {MAX_LINE_CHARS} cap"
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
