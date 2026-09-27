# Cloud server monitoring

servers = ["web-01", "web-02", "db-01", "api-01"]

# O(1) — direct access by index
first_server = servers[0]

# O(1) — add a server at the end
servers.append("cache-01")

# O(n) — search through the list
if "db-01" in servers:
    print("Database server found")

# O(n) — insert at the beginning
servers.insert(0, "load-balancer")

# O(n) — remove from the beginning
servers.pop(0)

print(first_server)
print(servers)
