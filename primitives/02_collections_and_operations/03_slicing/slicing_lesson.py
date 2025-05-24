# Examples and use cases for Slicing

# --- Examples ---

lst = [10, 20, 30, 40, 50, 60]
print(lst[2:5])    # [30, 40, 50]
print(lst[:3])     # [10, 20, 30]
print(lst[3:])     # [40, 50, 60]
print(lst[::2])    # [10, 30, 50]
print(lst[::-1])   # [60, 50, 40, 30, 20, 10]

s = "abcdefg"
print(s[1:5:2])    # "bd"

# --- Questions ---
# 1. What does lst[-3:] return if lst = [1, 2, 3, 4, 5, 6]?
# 2. How can you reverse a string using slicing?