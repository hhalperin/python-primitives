# Examples and use cases for Unpacking and Star Expressions

# --- Examples ---

# Basic unpacking
coords = (10, 20)
x, y = coords
print(f"Coordinates: ({x}, {y})")

# Unpacking with star expression
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print(f"First: {first}, Middle: {middle}, Last: {last}")

# Unpacking in a loop
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
for number, letter in pairs:
    print(f"Number: {number}, Letter: {letter}")

# Using * to unpack arguments
def greet(name, age, city):
    return f"{name} is {age} years old and lives in {city}."

person_info = ["Alice", 25, "New York"]
print(greet(*person_info))

# --- Questions ---
# 1. What happens if you try: a, b = [1, 2, 3, 4, 5]?
# 2. How would you use unpacking to swap the values of two variables without using a temporary variable?

a, *b = [1, 2, 3, 4, 5]
print(a, b)

a, b = b, a

