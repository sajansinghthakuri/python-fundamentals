# Stop when a failed server is found.

servers = {
    "web-01": "running",
    "web-02": "running",
    "db-01": "failed",
    "db-02": "running",
}

for server, status in servers.items():
    if status == "failed":
        print(f"Failure found: {server}")
        break
