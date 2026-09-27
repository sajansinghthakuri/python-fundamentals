# Return unique regions from server data.


def get_regions(servers: list[dict[str, str]]) -> set[str]:
    """Return unique server regions."""
    return {server["region"] for server in servers}


servers = [
    {"name": "web-01", "region": "ap-south-1"},
    {"name": "web-02", "region": "ap-south-1"},
    {"name": "db-01", "region": "us-east-1"},
]

print(get_regions(servers))
