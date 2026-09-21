# Arithmetic operators
a = 10
b = 3

print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")
print(f"Floor division: {a // b}")
print(f"Remainder: {a % b}")
print(f"Exponent: {a**b}")


# Comparison operators
x = 10
y = 5

# print(x == y)
# print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)


# Logical operators
age = 28
is_student = True

print(age >= 18 and is_student)
print(age < 18 or is_student)
print(not is_student)


# Assignment operators
score = 10

score += 5
print(score)

score -= 2
print(score)

score *= 2
print(score)

score //= 2
print(score)


# Exercise 1 — Shopping
price = 500
quantity = 3
print(f"Total: {price * quantity}")


# Exercise 2 — Remainder Calculate the remainder when divided by 5.
number = 27
remainder = number % 5
print(f"Remainder: {remainder}")


# Exercise 3 — Even/Odd
number = 24
is_even = number % 2 == 0
print(f"Is even: {is_even}")


# Exercise 4 — Comparisons Adult: True Senior: False
age = 28
is_adult = age >= 18
is_senior = age >= 65
print(f"Is adult: {is_adult}")
print(f"Is senior: {is_senior}")


# Exercise 5 — Logical operators Determine whether the person can drive:
age = 28
has_license = True
can_drive = age >= 18 and has_license
print(f"Can drive: {can_drive}")


result = 10 + 2 * 3**2
print(f"Result: {result}")
