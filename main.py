#!/usr/bin/env python3
"""The Worst App Idea Ever Pitched — one sentence, at most 240 characters.

Writes the pitch to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Python 3.13, standard library only, no network, deterministic output.
"""

import os
import sys

PITCH = (
    "DustWatch is a premium app that livestreams the dust settling on your "
    "bookshelf in 4K, sending a push alert every time a new speck lands, for "
    "collectors who must know the exact moment their belongings get dirty."
)


def main() -> int:
    text = PITCH.strip()
    if not 1 <= len(text) <= 240:
        print(f"pitch is {len(text)} chars, must be 1-240", file=sys.stderr)
        return 1
    if text != text.strip() or not text:
        print("pitch must not be only whitespace", file=sys.stderr)
        return 1
    if text.count(".") != 1 or not text.endswith(".") or "\n" in text:
        print("pitch must be exactly one sentence on one line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Clean only the CONTENTS of the output folder, never the folder itself:
    # the grader mounts that folder, removing it fails with EPERM.
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
    with open(os.path.join(out_dir, "entry.txt"), "w",
              encoding="utf-8", newline="") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
