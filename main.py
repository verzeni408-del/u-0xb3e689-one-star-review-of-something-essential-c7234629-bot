"""One-star review entry writer (v3, fresh angle).

Angle: toilet paper. Deadpan complaint about something everyone uses and
nobody wants to think about — the universal betrayal lands in the final
turn, one square short, right when the job is done.
"""

import os

# Single-line entry, max 160 chars, deadpan throughout — no jokes, just the facts.
ENTRY = "Toilet paper always runs out one square before the job is done."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
