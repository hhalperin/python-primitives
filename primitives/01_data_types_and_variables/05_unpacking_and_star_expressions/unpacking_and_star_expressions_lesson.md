# Unpacking and Star Expressions

## What is it?

Unpacking is a way to extract values from iterables (like lists or tuples) and assign them to variables in a single operation. Star expressions (using `*`) allow flexible unpacking by collecting multiple values into a list or expanding a sequence into individual elements.

## Examples

```python
# Basic unpacking
a, b, c = [1, 2, 3]
print(a, b, c)  # 1 2 3

# Swapping values without a temporary variable
a, b = b, a
print(a, b)  # 2 1

# Star expression to collect remaining values
first, *rest = [1, 2, 3, 4, 5]
print(first)  # 1
print(rest)   # [2, 3, 4, 5]

# Star in the middle
beginning, *middle, end = [1, 2, 3, 4, 5]
print(beginning, middle, end)  # 1 [2, 3, 4] 5

# Unpacking in for loops
points = [(1, 2), (3, 4), (5, 6)]
for x, y in points:
    print(f"X: {x}, Y: {y}")

# Unpacking function arguments
def add(a, b, c):
    return a + b + c
    
values = [1, 2, 3]
result = add(*values)  # Equivalent to add(1, 2, 3)
```

## Key Points

- Unpacking is concise and Pythonic.
- Use star expressions (`*`) to collect multiple values into a list.
- The starred variable can be at any position, but only one star expression is allowed per assignment.
- Useful for function arguments, return values, and parsing iterables.
- Common in loops, tuple assignments, and function calls. 