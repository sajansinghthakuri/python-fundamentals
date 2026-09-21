# Convert string to integer
age_text = "28"
age = int(age_text)

print(age)
print(type(age))


# Convert string to float
price_text = "99.99"
price = float(price_text)

print(price)
print(type(price))


# Convert number to string
age = 28
age_text = str(age)

print(age_text)
print(type(age_text))


# Convert values to boolean
print(bool(1))
print(bool(0))

print(bool("Python"))
print(bool(""))


# Process user information
name = "Sajan"
age_text = "28"
height_text = "5.9"

age = int(age_text)
height = float(height_text)

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")

# Exercise 1
year_text = "1997"
year = int(year_text)

print(f"Year: {year}")
print(f"Year type: {type(year)}")


# Exercise 2
price_text = "1499.50"
price = float(price_text)

print(f"Price: {price}")
print(f"Price type: {type(price)}")


# Exercise 3
number = 100
number_text = str(number)

print(f"Number: {number}")
print(f"Number type: {type(number)}")
print(f"Number as string: {number_text}")
print(f"Number as string type: {type(number_text)}")


# Exercise 4 Predict the result before running it:
print(bool(0))
print(bool(1))
print(bool(""))
print(bool("Python"))


# Exercise 5
age_text = "28"
age_next_year = int(age_text) + 1

print(f"Age next year: {age_next_year}")
print(f"Age in 5 years: {int(age_text) + 5}")


# Exercise 6
price_text = "1500"
quantity_text = "3"

price_int = int(price_text)
quantity_int = int(quantity_text)
total = price_int * quantity_int

print(f"Price: {price_int}")
print(f"Quantity: {quantity_int}")
print(f"Total: {total}")
