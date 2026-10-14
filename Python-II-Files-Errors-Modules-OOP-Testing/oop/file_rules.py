# Lab 4 — OOP, Inheritance, and Dataclasses
# Lab: Create rules that identify files by extension and size. This prepares you to design reusable rules for the File Organizer CLI.

from dataclasses import dataclass
from pathlib import Path


@dataclass
class FileRule:
    """Base class for file rules."""

    name: str

    def matches(self, file: Path) -> bool:
        """Check whether a file matches the rule."""
        raise NotImplementedError("Subclasses must implement matches()")


@dataclass
class ExtensionRule(FileRule):
    """Match files by extension."""

    extension: str

    def matches(self, file: Path) -> bool:
        return file.suffix.lower() == self.extension.lower()


@dataclass
class SizeRule(FileRule):
    """Match files larger than a specified size."""

    minimum_bytes: int

    def matches(self, file: Path) -> bool:
        return file.stat().st_size >= self.minimum_bytes


# Create sample files.
log_file = Path("server.log")
log_file.write_text("Server is healthy", encoding="utf-8")

# Create and test rules.
extension_rule = ExtensionRule(
    name="Log files",
    extension=".log",
)

size_rule = SizeRule(
    name="Files at least 10 bytes",
    minimum_bytes=10,
)

print("Extension match:", extension_rule.matches(log_file))
print("Size match:", size_rule.matches(log_file))
print("Rule name:", extension_rule.name)
