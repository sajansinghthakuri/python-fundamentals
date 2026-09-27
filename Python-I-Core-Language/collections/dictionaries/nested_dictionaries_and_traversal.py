servers = {
    "web-01": {"status": "running", "port": 80},
    "db-01": {"status": "running", "port": 5432},
}

for name, details in servers.items():
    print(f"{name}: {details['status']}")
