# Skip stopped servers.

servers = {
    "web-01": "running",
    "web-02": "stopped",
    "db-01": "running",
}

for server, status in servers.items():
    if status == "stopped":
        continue

    print(f"Checking {server}")
