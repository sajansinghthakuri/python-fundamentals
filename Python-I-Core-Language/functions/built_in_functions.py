# Cloud/DevOps: Analyze server health

# Server health scores
health_scores = [95, 82, 67, 91, 76]

# Server status
statuses = ["running", "running", "stopped", "running", "running"]

# Server names
servers = ["web-03", "web-01", "db-02", "web-02", "db-01"]


# Number of servers
print("Total servers:", len(servers))

# Health statistics
print("Total health:", sum(health_scores))
print("Lowest health:", min(health_scores))
print("Highest health:", max(health_scores))

# Check whether any server is stopped
has_stopped_server = any(status == "stopped" for status in statuses)
print("Has stopped server:", has_stopped_server)

# Check whether every server is running
all_running = all(status == "running" for status in statuses)
print("All servers running:", all_running)

# Increase every health score by 5
updated_scores = list(map(lambda score: score + 5, health_scores))
print("Updated scores:", updated_scores)

# Keep only healthy servers
healthy_scores = list(filter(lambda score: score >= 80, health_scores))
print("Healthy scores:", healthy_scores)

# Sort server names alphabetically
sorted_servers = sorted(servers)
print("Sorted servers:", sorted_servers)

# Reverse server order
reverse_servers = list(reversed(servers))
print("Reverse order:", reverse_servers)
