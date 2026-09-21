print(bool(10))
print(bool(0))

# Common falsy values
print(False)
print(bool(None))
print(bool(0))
print(bool(0.0))
print(bool(""))
print(bool([]))
print(bool(()))
print(bool({}))
# print(bool(set()))


# Common truthy values
print(True)
print(bool(1))
print(bool(-1))
print(bool(3.14))
print(bool("Python"))
print(bool([1, 2, 3]))
print(bool((1, 2)))
print(bool({"name": "Sajan"}))


# Exercise 1 — Predict
print(bool(0))
print(bool(1))
print(bool(""))
print(bool("Python"))
print(bool([]))
print(bool([1]))
print(bool(None))


# Exercise 2 — Server list print Servers available
servers = ["web-01", "web-02"]
if servers:
    print("Servers available:")
    for server in servers:
        print(f" - {server}")
else:
    print("No servers available.")


# Exercise 3 — == vs is
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(a is b)


# Exercise 4 — None

result = None

if result is None:
    print("No result")

result = "Success"

# if result is not None:
#     print("Result available")


# Exercise 5 — Mutable default argument
# def add_item(item, items=[]):
#     items.append(item)
#     return items


# print(add_item("Python"))
# print(add_item("Linux"))


items = []

# print(bool(items))

# items.append("Python")

# print(bool(items))
# print(items)

value = None

print(value is None)
print(value == None)
