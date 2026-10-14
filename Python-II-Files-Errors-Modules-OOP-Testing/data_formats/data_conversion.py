# Lab 2 — CSV, JSON, and YAML
# Lab: Read server data from a CSV file, convert it into Python dictionaries, and save it as JSON. Then save configuration data as YAML.
import csv
import json
from pathlib import Path

import yaml

# Create sample server data.
csv_file = Path("servers.csv")

csv_file.write_text(
    "name,status,region\n"
    "web-01,healthy,ap-south\n"
    "web-02,warning,ap-south\n"
    "db-01,healthy,ap-east\n",
    encoding="utf-8",
)

# Read CSV rows into dictionaries.
with csv_file.open(
    "r",
    newline="",
    encoding="utf-8",
) as file:
    servers = list(csv.DictReader(file))

# Save the data as JSON.
json_file = Path("servers.json")

with json_file.open("w", encoding="utf-8") as file:
    json.dump(servers, file, indent=4)

# Read the JSON data.
with json_file.open("r", encoding="utf-8") as file:
    loaded_servers = json.load(file)

print("Server count:", len(loaded_servers))
print("First server:", loaded_servers[0])

# Create configuration data.
config = {
    "log_directory": "logs",
    "allowed_extensions": [".log", ".txt"],
}

# Save configuration as YAML.
yaml_file = Path("config.yaml")

with yaml_file.open("w", encoding="utf-8") as file:
    yaml.safe_dump(config, file)

# Read configuration from YAML.
with yaml_file.open("r", encoding="utf-8") as file:
    loaded_config = yaml.safe_load(file)

print("Log directory:", loaded_config["log_directory"])
print("Allowed extensions:", loaded_config["allowed_extensions"])
