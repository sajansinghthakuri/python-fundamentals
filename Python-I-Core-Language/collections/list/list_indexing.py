# Keep servers in a fixed order for this inventory
servers = ["web-01", "web-02", "app-01", "db-01"]

# Positive indexes count from the beginning
print("First:", servers[0])
print("Second:", servers[1])
print("Third:", servers[2])
print("Fourth:", servers[3])

# Negative indexes count backward from the end
print("Last:", servers[-1])
print("Second-last:", servers[-2])
print("Third-last:", servers[-3])
