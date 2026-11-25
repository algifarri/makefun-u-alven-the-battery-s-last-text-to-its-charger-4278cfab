#!/usr/bin/env python3
"""Entry for make.fun bounty u-alven-the-battery-s-last-text-to-its-charger-4278cfab.

Writes one line to /output/entry.txt: the phone battery's last text message
to the charger it waited for all day. Deterministic, stdlib-only, no network,
no randomness, no environment reads. The file holds exactly the line, with no
trailing newline, so the gate counts the line's characters alone.
"""

import os

LINE = (
    "Left me at 2% all day while you charged your watch, your vape, "
    "and your AirPods twice. Plug me in now, or your 6 a.m. alarm dies with me."
)


def main() -> None:
    # The gate accepts 1 to 200 characters; fail loudly instead of
    # shipping a line the judge never sees. Count in characters, not
    # bytes, exactly as the gate does.
    if not 1 <= len(LINE) <= 200:
        raise SystemExit(f"line is {len(LINE)} characters, outside 1-200")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
