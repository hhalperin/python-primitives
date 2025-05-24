# 3 Basic Operations

## What is it?

Basic operations in Python include arithmetic, comparison, logical, and assignment operations. These are the fundamental building blocks for manipulating data and controlling program flow.

- **Arithmetic operations**: +, -, *, /, //, %, **
- **Comparison operations**: ==, !=, <, >, <=, >=
- **Logical operations**: and, or, not
- **Assignment operations**: =, +=, -=, etc.

## Examples

```python
# Arithmetic
x = 10 + 5      # 15
x = 10 - 3      # 7
x = 2 * 3       # 6
x = 7 / 2       # 3.5
x = 7 // 2      # 3 (integer division)
x = 7 % 2       # 1 (modulo)
x = 2 ** 3      # 8 (exponentiation)

# Comparison
a = 5
b = 10
print(a < b)    # True
print(a == b)   # False

# Logical
print(True and False)  # False
print(True or False)   # True
print(not True)        # False

# Assignment
x = 5
x += 2  # x = x + 2
print(x)  # 7
```

## Key Points

- Arithmetic operations work on numbers (int, float).
- Comparison operations return a boolean value.
- Logical operations combine or invert boolean values.
- Assignment operations can combine with arithmetic (+=, -=, etc.).
- Operator precedence determines the order of evaluation (use parentheses to clarify).
