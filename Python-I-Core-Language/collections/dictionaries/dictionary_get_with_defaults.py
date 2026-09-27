server = {"name": "web-01", "status": "running"}

print(server.get("name"))
print(server.get("ip", "Not configured"))
