"""Frost Robot Band — a one-liner entry for make.fun's Name the Robot Band.

Writes exactly one funny robot band name, plus a few words on its hit
song, to entry.txt. The text stays well under the 200-character gate.
"""

import os

LINE = 'CTRL+ALT+DEFEAT \u2014 hit single "Have You Tried Turning Me Off and On Again?" \u2014 their farewell tour ended when someone actually did.'

assert 1 <= len(LINE) <= 200, "entry line must be 1-200 characters"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
