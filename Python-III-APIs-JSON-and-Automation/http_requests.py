import json

import requests


def inspect_api(
    name: str,
    url: str,
    params: dict[str, str] | None = None,
) -> None:
    """Send a GET request and inspect the API response."""

    print(f"\n--- {name} ---")

    try:
        response = requests.get(
            url,
            params=params,
            timeout=10,
        )

        print("URL:", response.url)
        print("Status Code:", response.status_code)
        print("Content Type:", response.headers.get("Content-Type"))

        response.raise_for_status()

        data = response.json()

        print("Response:")

        if isinstance(data, dict):
            print(json.dumps(data, indent=4)[:500])
        else:
            print(json.dumps(data, indent=4)[:500])

    except requests.exceptions.Timeout:
        print("Error: Request timed out.")

    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the server.")

    except requests.exceptions.HTTPError as error:
        print("HTTP Error:", error)

    except requests.exceptions.RequestException as error:
        print("Request Error:", error)


inspect_api(
    "GitHub API",
    "https://api.github.com/repos/python/cpython",
)

inspect_api(
    "JSONPlaceholder API",
    "https://jsonplaceholder.typicode.com/posts/1",
)

inspect_api(
    "HTTPBin API",
    "https://httpbin.org/get",
    params={"course": "Python III", "day": "1"},
)
inspect_api(
    "HTTP Error Test",
    "https://jsonplaceholder.typicode.com/invalid-endpoint",
)
# Timeout Error Test
print("\n--- Timeout Error Test ---")

try:
    requests.get(
        "https://httpbin.org/delay/3",
        timeout=1,
    )

except requests.exceptions.Timeout:
    print("Error: Request timed out.")


# Connection Error Test
print("\n--- Connection Error Test ---")

try:
    requests.get(
        "https://this-domain-does-not-exist.invalid",
        timeout=5,
    )

except requests.exceptions.ConnectionError:
    print("Error: Could not connect to the server.")
