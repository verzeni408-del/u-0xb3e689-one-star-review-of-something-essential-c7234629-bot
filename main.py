"""One-star review generator, fourth draft.

Assembles one deadpan complaint about a daily essential and drops it
into the submission file the harness reads.
"""

import os

OUT_DIR = "/output"
OUT_FILE = os.path.join(OUT_DIR, "entry.txt")

REVIEW = (
    "My toothbrush reaches every tooth "
    "except the one the dentist always asks about."
)


def _prepare(folder):
    if not os.path.isdir(folder):
        os.makedirs(folder, exist_ok=True)


def _emit(text, path):
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
        handle.write("\n")


def build():
    _prepare(OUT_DIR)
    _emit(REVIEW, OUT_FILE)
    return OUT_FILE


if __name__ == "__main__":
    build()
