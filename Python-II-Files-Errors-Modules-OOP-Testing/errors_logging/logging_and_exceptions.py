# Lab 3 — Exceptions and Logging
# Lab: Read a configuration file safely. If it does not exist, log an error rather than allowing an unhandled exception to terminate the script.
import logging
from pathlib import Path

# Configure logging.
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s",
    datefmt="%H:%M:%S",
)

config_file = Path("config.txt")

try:
    content = config_file.read_text(encoding="utf-8")

except FileNotFoundError:
    logging.error("Configuration file not found: %s", config_file)

except PermissionError:
    logging.error("Permission denied: %s", config_file)

else:
    logging.info("Configuration loaded successfully")
    print(content)

finally:
    logging.info("Configuration check finished")
