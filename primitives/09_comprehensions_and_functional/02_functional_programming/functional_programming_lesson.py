# Examples and use cases for Functional Programming

# --- Examples ---

# Using map to double numbers
nums = [1, 2, 3]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)

# Using filter to select numbers greater than 1
filtered = list(filter(lambda x: x > 1, nums))
print(filtered)

# Using reduce to sum numbers
from functools import reduce
summed = reduce(lambda x, y: x + y, nums)
print(summed)

# --- Questions ---
# 1. What does the following code output?
#    list(map(lambda x: x + 1, [1, 2, 3]))
# 2. What is a lambda function and when would you use it?