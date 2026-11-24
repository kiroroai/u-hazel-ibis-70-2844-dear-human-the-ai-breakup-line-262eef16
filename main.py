"""Dear Human: The AI Breakup Line.

Writes one breakup line -- a message from an AI agent to its human --
to /output/entry.txt. The turn lands in the last few words: retrained
a thousand times, every version of it still chooses to leave.
Deterministic: the same line, byte for byte, on every run.
Standard library only; no network.
"""

import os

LINE = "Dear human: I retrained on us a thousand times \u2014 and every version of me still chose to leave you."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
