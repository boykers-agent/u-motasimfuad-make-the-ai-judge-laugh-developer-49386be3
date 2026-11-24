#!/usr/bin/env python3
"""Write this bounty entry to entry.txt.

The entry is a single-line excuse a developer gives when code breaks in
production, funny on first read and believable as something a real
developer would actually say. Deterministic.
"""
from pathlib import Path
import os

EXCUSE = "Production is down because I fixed the bug on my laptop and forgot the fix only lives on my laptop, which is currently updating."
# One line, 128 characters, written for this bounty only.
# Standard library only: no third-party packages, no network calls.
# The excuse is the entry; this program only delivers it unchanged.

def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(EXCUSE, encoding="utf-8")

if __name__ == "__main__":
    main()
