# Check the status of multiple servers.


def check_servers(*servers):
    for server in servers:
        print(f"Checking {server}")


check_servers("web-01", "web-02", "db-01")
