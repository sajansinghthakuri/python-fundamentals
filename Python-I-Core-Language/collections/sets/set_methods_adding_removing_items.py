servers = {"web-01", "web-02"}

servers.add("web-03")
servers.update(["db-01", "db-02"])

servers.remove("web-03")
servers.discard("cache-01")  # Safe if item doesn't exist

print(servers)
