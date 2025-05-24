# Examples and use cases for Mutability vs. Immutability

# --- Examples ---

# Mutable example: list
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)  # [1, 2, 3, 4]
numbers[0] = 100
print(numbers)  # [100, 2, 3, 4]

# Immutable example: string
word = "hello"
# word[0] = 'H'  # This would raise a TypeError
word = "Hello"  # This is a new string object
print(word)

# Immutable example: tuple
t = (1, 2, 3)
# t[0] = 10  # This would raise a TypeError

# --- Questions ---
# 1. What happens if you try to change an element of a tuple?
# 2. Why is it dangerous to use a mutable object as a default argument in a function?