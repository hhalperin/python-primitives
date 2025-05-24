# Examples and use cases for Basic Recursion

# --- Examples ---

# Recursive factorial
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(4))  # 24

# Recursive sum of a list
def recursive_sum(lst):
    if not lst:
        return 0
    return lst[0] + recursive_sum(lst[1:])

print(recursive_sum([1, 2, 3, 4]))  # 10

# --- Questions ---
# 1. What is a base case in recursion, and why is it important?
# 2. What will happen if a recursive function does not have a base case?