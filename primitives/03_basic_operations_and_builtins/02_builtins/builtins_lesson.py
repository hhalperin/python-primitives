# Examples and use cases for Built-in Functions

# --- Examples ---

numbers = [10, 20, 30]
print(len(numbers))      # 3
print(sum(numbers))      # 60
print(min(numbers))      # 10
print(max(numbers))      # 30
print(sorted(numbers, reverse=True))  # [30, 20, 10]

s = "python"
print(list(s))          # ['p', 'y', 't', 'h', 'o', 'n']
print(type(numbers))     # <class 'list'>

for idx, val in enumerate(numbers):
    print(idx, val)

# --- Questions ---
# 1. What does the zip() function do?
# 2. How can you get the absolute value of a number in Python?