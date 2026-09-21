# Create strings
name = "Sajan"
language = "Python"
country = "Nepal"

print(name)
print(language)
print(country)

# Check the type
print(type(name))

# Practice
first_name = "Sajan"
last_name = "Singh"

full_name = f"{first_name} {last_name}"

print(f"Full name: {full_name}")
print(f"Name length: {len(full_name)}")
print(f"Uppercase: {full_name.upper()}")
print(f"Lowercase: {full_name.lower()}")

# Indexing
print(f"First character: {first_name[0]}")
print(f"Last character: {first_name[-1]}")


# Slicing
print(f"First three characters: {first_name[:3]}")
print(f"Last two characters: {first_name[-2:]}")


# String methods
message = "  Python is powerful  "

print(message.strip())
print(message.strip().upper())
print(message.replace("powerful", "useful"))


# Joining strings
languages = ["Python", "Java", "Go"]

result = ", ".join(languages)

print(result)

# Practice
email = "  SAJAN@EXAMPLE.COM  "

# Remove surrounding whitespace and convert to lowercase.
print(f"email: {email.strip().lower()}")

# Extract the username from the email.
print(f"Username: {email.strip()[:5].lower()}")


# Check whether the email contains "@"
print("@" in email)

# Create this string: Python | Linux | Networking | Cloud
skills = ["Python", "Linux", "Networking", "Cloud"]
result = " | ".join(skills)
print(f"Skills: {result}")


# Reverse text = "Cloud Engineer"
text = "Cloud Engineer"
print(text[::-1])
