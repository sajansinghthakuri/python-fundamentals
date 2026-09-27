servers = ["web-01", "web-02", "db-01"]

for number, server in enumerate(servers, start=1):
    print(f"{number}. {server}")
