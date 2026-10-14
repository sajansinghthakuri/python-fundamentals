from pathlib import Path

from server_utils import get_log_files, get_timestamp


def main() -> None:
    """Display log files and the current timestamp."""
    logs_dir = Path("logs")

    for file in get_log_files(logs_dir):
        print("Log file:", file)

    print("Checked at:", get_timestamp())


if __name__ == "__main__":
    main()
