# Server inventory
servers = ["web-01", "web-02", "app-01", "db-01", "cache-01"]

# remove() deletes the first matching server
servers.remove("web-02")

# pop() removes the item at index 1 and gives it back
removed_server = servers.pop(1)

# pop() without an index removes the last server
last_server = servers.pop()

print("Removed:", removed_server)
print("Last removed:", last_server)
print("Remaining:", servers)
