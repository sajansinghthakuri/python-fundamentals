# Normal loop
servers = [
    {"name": "web-01", "region": "ap-south-1"},
    {"name": "web-02", "region": "ap-south-1"},
    {"name": "db-01", "region": "us-east-1"},
]

# regions = set()

# for server in servers:
#     regions.add(server["region"])

# Set comprehension
regions = {server["region"] for server in servers}
print(regions)
