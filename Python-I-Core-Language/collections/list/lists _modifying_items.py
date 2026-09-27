# Keep the server inventory in a fixed order
servers = ["web-01", "web-02", "app-01", "db-01"]

# Replace the second server with its new name
servers[1] = "web-prod-01"

# Replace the last server using negative indexing
servers[-1] = "db-prod-01"

print(servers)
