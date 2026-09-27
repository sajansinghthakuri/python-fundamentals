# Return only healthy servers.


def get_healthy_servers(
    health: dict[str, int],
) -> list[str]:
    """Return servers with health scores of 80 or higher."""
    return [server for server, score in health.items() if score >= 80]


health = {
    "web-01": 95,
    "web-02": 60,
    "db-01": 90,
}

print(get_healthy_servers(health))
