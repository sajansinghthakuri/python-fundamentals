# Lab 1 — File I/O and pathlib
# Lab: Practise creating files, writing and appending content, reading files, and finding files by extension.


from pathlib import Path

# Create a directory for log files.
logs_dir = Path("logs")
logs_dir.mkdir(parents=True, exist_ok=True)

# Create a log file.
log_file = logs_dir / "server.log"

# Write content to the file.
log_file.write_text(
    "web-01: healthy\nweb-02: warning\n",
    encoding="utf-8",
)

# Append another line.
with log_file.open("a", encoding="utf-8") as file:
    file.write("web-03: healthy\n")

# Read the file line by line.
with log_file.open("r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())

# Display file properties.
print("Exists:", log_file.exists())
print("Name:", log_file.name)
print("Extension:", log_file.suffix)
print("Stem:", log_file.stem)

# Find all log files in the directory tree.
for file in logs_dir.rglob("*.log"):
    print("Found:", file)
