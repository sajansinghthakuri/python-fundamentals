# Normal loop
servers = {
    "web-01": "running",
    "web-02": "stopped",
    "db-01": "running",
}

# running_servers = []

# for server, status in servers.items():
#     if status == "running":
#         running_servers.append(server)


# Comprehension
running_servers = [server for server, status in servers.items() if status == "running"]
print(running_servers)
