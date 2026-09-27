# Return the status of a server.


def get_server_status(
    servers: dict[str, str],
    server: str,
) -> str:
    """Return the status of a server."""
    return servers.get(server, "unknown")


servers = {
    "web-01": "running",
    "db-01": "stopped",
}

print(get_server_status(servers, "web-01"))
