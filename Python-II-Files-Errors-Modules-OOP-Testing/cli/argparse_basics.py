# Lab 7 — Command-Line Arguments with argparse
# Lab
# Build a small command-line interface that accepts a source directory, a destination directory, and a dry-run option.
# A dry run previews an operation without actually changing files. This will be a key requirement of our File Organizer CLI.


import argparse
from pathlib import Path


def main() -> None:
    """Read and validate command-line arguments."""

    parser = argparse.ArgumentParser(
        description="Preview a file organization operation."
    )

    parser.add_argument(
        "--source",
        type=Path,
        required=True,
        help="Directory containing the source files.",
    )

    parser.add_argument(
        "--dest",
        type=Path,
        required=True,
        help="Directory for the organized files.",
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without modifying files.",
    )

    args = parser.parse_args()

    print(f"Source: {args.source}")
    print(f"Destination: {args.dest}")

    if args.dry_run:
        print("Mode: Preview only")
    else:
        print("Mode: Normal execution")


if __name__ == "__main__":
    main()
