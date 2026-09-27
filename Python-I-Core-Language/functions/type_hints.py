# Check whether a server is running.


def check_server(server: str, status: str) -> bool:
    """Return True when the server is running."""

    return status == "running"


is_healthy = check_server("web-01", "running")

print(is_healthy)
