"""Write the apology one-liner to the entry file.

The program takes no input and reads nothing outside this file. It
writes one fixed line, exactly as it stands, with no added newline,
so the grader sees the same bytes on every run.
"""

import os
from pathlib import Path

ENTRY = "I emailed the boss your draft, then deleted it. Now only he has it."


def entry_path() -> Path:
    """Return where the line goes: /output unless overridden."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return Path(directory) / "entry.txt"


def main() -> None:
    path = entry_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
