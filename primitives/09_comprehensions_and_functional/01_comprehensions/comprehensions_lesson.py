# Examples and use cases for Comprehensions

# --- Examples ---

# List comprehension: squares of numbers 0-4
squares = [x**2 for x in range(5)]
print(squares)

# Set comprehension: unique first letters
words = ["apple", "banana", "apricot"]
first_letters = {w[0] for w in words}
print(first_letters)

# Dictionary comprehension: mapping numbers to their cubes
cubes = {x: x**3 for x in range(4)}
print(cubes)

# --- Questions ---
# 1. Rewrite this loop as a list comprehension:
#    result = []
#    for x in range(10):
#        if x % 3 == 0:
#            result.append(x)
# 2. What is the main advantage of using comprehensions over traditional loops?