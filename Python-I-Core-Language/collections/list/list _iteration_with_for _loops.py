servers = [
    "web-01",
    "web-02",
    "web-03",
    "db-01",
    "db-02",
    "cache-01",
]

# Check every server in the inventory.
for server in servers:
    print(f"Checking {server}...")

print("Inventory check complete.")
