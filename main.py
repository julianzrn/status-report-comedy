"""Entry for make.fun's "Status Report Comedy Sprint".

Running this program writes the entry line to /output/entry.txt.
"""

from pathlib import Path

REPORT = "This week I automated myself out of 40% of my job "
CONSEQUENCE = "and used the free time to write you this longer status report."

ENTRY = REPORT + CONSEQUENCE

OUTPUT_PATH = Path("/output/entry.txt")


def write_entry(path: Path = OUTPUT_PATH) -> None:
    """Write the entry line to the output file, with no trailing newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
