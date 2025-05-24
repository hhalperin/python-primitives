# Comments

## What is it?

Comments are notes in your code that are ignored by Python but help humans understand what the code does. Comments are essential for explaining logic, marking TODOs, and making code more maintainable.

Python supports single-line comments (using `#`) and multi-line comments (using triple quotes, though these are technically docstrings).

## Examples

```python
# This is a single-line comment
x = 5  # This is an inline comment

"""
This is a multi-line comment or docstring.
It can span several lines.
"""

def add(a, b):
    """Return the sum of a and b."""
    return a + b
```

## Key Points

- Use `#` for single-line comments.
- Use triple quotes (`'''` or `"""`) for multi-line comments or docstrings.
- Comments should explain why, not just what.
- Good comments make code easier to read and maintain.
- Docstrings are used for documentation and can be accessed with `help()`.
