import os
from pathlib import Path

FINAL_LINE = "He emailed the decision at 9:00, then called an hour-long meeting so twelve of us could watch him read that email aloud, in person, and slower."


def emit(line: str) -> None:
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target_dir.mkdir(parents=True, exist_ok=True)
    (target_dir / "entry.txt").write_text(line, encoding="utf-8")


if __name__ == "__main__":
    emit(FINAL_LINE)
