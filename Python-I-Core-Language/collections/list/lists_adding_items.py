# Start with the servers currently in our inventory
servers = ["web-01", "web-02", "db-01"]

# append() adds one new server to the end
servers.append("cache-01")

# insert() adds a server at index 1
servers.insert(1, "app-01")

# extend() adds multiple servers at once
servers.extend(["db-02", "db-03"])

print(servers)
