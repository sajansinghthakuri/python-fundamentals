server_groups = [
    ["web-01", "web-02"],
    ["db-01", "db-02"],
]

for group in server_groups:
    for server in group:
        print(f"Checking {server}")
