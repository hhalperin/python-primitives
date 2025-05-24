# PEP8 and Pythonic Code

## What is it?

PEP8 is the official style guide for Python code. It provides conventions for writing readable, consistent, and maintainable code. "Pythonic" code refers to code that follows these conventions and uses idiomatic Python constructs.

Following PEP8 and writing Pythonic code makes your programs easier to read, share, and maintain.

## Examples

```python
# Good (PEP8-compliant, Pythonic)
def add_numbers(a, b):
    return a + b

result = add_numbers(2, 3)

# Bad (not PEP8-compliant)
def addNumbers(a,b): return a+b
result=addNumbers(2,3)

# Pythonic: use list comprehensions
squares = [x**2 for x in range(5)]

# Not Pythonic: use loops for simple tasks
squares = []
for x in range(5):
    squares.append(x**2)
```

## Key Points

- Use 4 spaces per indentation level (no tabs).
- Use lowercase_with_underscores for function and variable names.
- Keep lines under 79 characters.
- Add spaces around operators and after commas.
- Use docstrings for functions and modules.
- Prefer list comprehensions, `enumerate()`, and unpacking for clarity.
- Readable code is better than clever code.
- Use tools like `flake8` or `black` to check/enforce style.
