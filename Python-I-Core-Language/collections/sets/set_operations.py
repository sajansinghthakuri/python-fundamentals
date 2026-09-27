production = {"web-01", "web-02", "db-01"}
backup = {"web-02", "db-01", "cache-01"}

print(production | backup)
print(production & backup)
print(production - backup)
