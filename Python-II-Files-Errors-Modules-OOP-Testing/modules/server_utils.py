# Lab 5 — Modules and the Standard Library
from datetime import datetime
from pathlib import Path


def get_log_files(directory: Path) -> list[Path]:
    """Return all log files in a directory tree."""
    return list(directory.rglob("*.log"))


def get_timestamp() -> str:
    """Return the current date and time."""
    return datetime.now().isoformat(timespec="seconds")
