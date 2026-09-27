servers = ["web-01", "web-02"]

# Create an independent copy
backup = servers.copy()

backup.append("db-01")

print("Servers:", servers)
print("Backup:", backup)
