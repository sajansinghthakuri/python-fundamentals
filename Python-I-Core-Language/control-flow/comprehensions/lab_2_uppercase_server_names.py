# Normal loop
servers = ["web-01", "web-02", "db-01"]

# server_names = []

# for server in servers:
#     server_names.append(server.upper())


# Comprehension
server_names = [server.upper() for server in servers]
print(server_names)
