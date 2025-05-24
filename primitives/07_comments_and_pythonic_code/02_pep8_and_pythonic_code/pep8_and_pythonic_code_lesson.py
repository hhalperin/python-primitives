# Examples and use cases for PEP8 and Pythonic Code

# --- Examples ---

# Good: PEP8-compliant
my_list = [1, 2, 3]
for item in my_list:
    print(item)

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

# Bad: Not PEP8-compliant
myList=[1,2,3]
for item in myList:print(item)
def multiplyNumbers(a,b):return a*b

# Pythonic: use enumerate
for idx, value in enumerate(my_list):
    print(idx, value)

# --- Questions ---
# 1. What is the recommended indentation in Python according to PEP8?
# 2. Why is it better to use list comprehensions instead of loops for simple list transformations?