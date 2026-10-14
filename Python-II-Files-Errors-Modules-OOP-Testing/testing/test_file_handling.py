from pathlib import Path

import pytest


def get_extension(file: Path) -> str:
    """Return a file's extension."""
    return file.suffix.lower()


def read_file(file: Path) -> str:
    """Read a text file."""
    return file.read_text(encoding="utf-8")


@pytest.fixture
def sample_file(tmp_path: Path) -> Path:
    """Create a temporary log file for testing."""
    file = tmp_path / "server.log"
    file.write_text("Server is healthy", encoding="utf-8")
    return file


# Test 1: Check the file extension.
def test_get_extension(sample_file: Path) -> None:
    assert get_extension(sample_file) == ".log"


# Test 2: Check that the file content is read correctly.
def test_read_file(sample_file: Path) -> None:
    assert read_file(sample_file) == "Server is healthy"


# Test 3: Check that the temporary file exists.
def test_file_exists(sample_file: Path) -> None:
    assert sample_file.exists()


# Test 4: Check multiple file extensions.
@pytest.mark.parametrize(
    ("filename", "expected"),
    [
        ("server.log", ".log"),
        ("config.yaml", ".yaml"),
        ("servers.csv", ".csv"),
        ("backup.JSON", ".json"),
    ],
)
def test_get_extension_variants(
    filename: str,
    expected: str,
) -> None:
    file = Path(filename)

    assert get_extension(file) == expected
