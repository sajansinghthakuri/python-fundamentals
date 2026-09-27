# Return a message based on server status.


def check_server(status: str) -> str:
    """Return a message for a server status."""
    if status == "running":
        return "Server is healthy."
    elif status == "stopped":
        return "Server is stopped."
    else:
        return "Unknown status."


print(check_server("running"))
