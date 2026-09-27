servers = [
    {"name": "web-01", "memory": 8},
    {"name": "web-02", "memory": 16},
    {"name": "db-01", "memory": 32},
]

sorted_servers = sorted(servers, key=lambda server: server["memory"])

for server in sorted_servers:
    print(server["name"], server["memory"], "GB")
