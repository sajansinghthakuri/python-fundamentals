server_group = ("production", ["web-01", "web-02"])

# The tuple stays fixed, but the nested list can change.
server_group[1].append("web-03")

print(server_group)
