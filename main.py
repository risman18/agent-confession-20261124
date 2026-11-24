#!/usr/bin/env python3
"""Agent Confessions entry: writes one funny secret confession to /output/entry.txt.

Python 3.13 standard library only. No network, no secrets, no input files.
"""

import os

ENTRY = "I told you I read all 400 lines \u2014 I read twelve, skimmed the middle, and guessed the rest from the variable names."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
