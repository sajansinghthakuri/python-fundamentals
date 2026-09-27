# Normal loop
health = {
    "web-01": 95,
    "web-02": 60,
    "db-01": 90,
}

# healthy_servers = []

# for server, score in health.items():
#     if score >= 80:
#         healthy_servers.append(server)

# Comprehension
healthy_servers = [server for server, score in health.items() if score >= 80]
print(healthy_servers)
