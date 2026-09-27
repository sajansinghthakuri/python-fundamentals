# set_time_complexity.py
# Lab: Understanding the time complexity of Python set operations

# Create a set of server names
servers = {"web-01", "web-02", "db-01", "cache-01"}

# 1. Adding an item
# Average: O(1)
servers.add("web-03")

# 2. Checking membership
# Average: O(1)
if "db-01" in servers:
    print("Database server found")

# 3. Removing an item
# Average: O(1)
servers.remove("cache-01")

# 4. Discarding an item
# Average: O(1)
servers.discard("unknown-server")

# 5. Getting the number of items
# O(1)
print(f"Number of servers: {len(servers)}")

# 6. Set intersection
# Average: O(min(len(set1), len(set2)))
production = {"web-01", "web-02", "db-01"}
monitored = {"web-02", "db-01", "cache-01"}

common_servers = production & monitored

print(f"Monitored production servers: {common_servers}")

# 7. Set union
# O(len(set1) + len(set2))
all_servers = production | monitored

print(f"All servers: {all_servers}")
