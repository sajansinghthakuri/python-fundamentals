# Store the servers in the order we manage them
servers = ["web-01", "web-02", "db-01"]

# Index 0 gives the first server
print("First server:", servers[0])

# Negative index -1 gives the last server
print("Last server:", servers[-1])

# len() returns the number of servers
print("Total servers:", len(servers))
