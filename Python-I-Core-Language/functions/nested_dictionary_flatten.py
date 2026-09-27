# Flatten nested cloud server data.


def flatten_dict(
    data: dict,
    parent_key: str = "",
    separator: str = "_",
) -> dict:
    """Flatten a nested dictionary into a single-level dictionary."""

    flattened = {}

    for key, value in data.items():
        new_key = f"{parent_key}{separator}{key}" if parent_key else key

        if isinstance(value, dict):
            flattened.update(flatten_dict(value, new_key, separator))
        else:
            flattened[new_key] = value

    return flattened


server = {
    "name": "web-01",
    "details": {
        "region": "ap-south-1",
        "status": "running",
        "resources": {
            "cpu": 4,
            "memory": 8,
        },
    },
}

result = flatten_dict(server)

print(result)
