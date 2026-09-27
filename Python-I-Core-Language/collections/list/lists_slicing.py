# Cloud infrastructure inventory
servers = [
    "web-01",
    "web-02",
    "web-03",
    "db-01",
    "db-02",
    "cache-01",
]

# Get the first three servers
frontend_servers = servers[:3]

# Get the database servers
database_servers = servers[3:5]

# Get the last three servers
last_servers = servers[-3:]

# Get every second server
alternate_servers = servers[::2]

# Create a reversed copy of the inventory
reversed_servers = servers[::-1]

print("All servers:", servers)
print("Frontend servers:", frontend_servers)
print("Database servers:", database_servers)
print("Last three servers:", last_servers)
print("Alternate servers:", alternate_servers)
print("Reversed inventory:", reversed_servers)
