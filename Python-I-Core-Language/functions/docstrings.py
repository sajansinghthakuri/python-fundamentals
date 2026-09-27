def check_server_status(server):
    """
    Return the status message for a server.

    Args:
        server: Server name.

    Returns:
        A server status message.
    """
    return f"{server} is running"


status = check_server_status("web-01")

print(status)
