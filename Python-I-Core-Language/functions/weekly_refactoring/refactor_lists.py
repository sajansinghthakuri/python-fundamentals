# Return servers sorted alphabetically.


def sort_servers(servers: list[str]) -> list[str]:
    """Return servers in alphabetical order."""
    return sorted(servers)


servers = ["web-02", "db-01", "web-01"]

result = sort_servers(servers)

print(result)
