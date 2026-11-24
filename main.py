#!/usr/bin/env python3
"""Say What Actually Broke — one line of honest error copy.

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
The line names the real failure in plain words: the file is 2 GB, the form
accepts 10 MB, and here is what to do about it.
"""

import os

ENTRY = (
    "This file is 2 GB. The form accepts 10 MB. You tried to push a feature "
    "film through a keyhole; shrink it, split it, or send a link instead."
)


def check_gate(text: str) -> None:
    """Mirror the bounty gate: UTF-8 text of 1 to 200 characters, a single
    line, and not only white space."""
    assert 1 <= len(text) <= 200, "entry must be 1 to 200 characters"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only white space"
    text.encode("utf-8")


def main() -> None:
    check_gate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY)
    print(f"wrote {path} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
