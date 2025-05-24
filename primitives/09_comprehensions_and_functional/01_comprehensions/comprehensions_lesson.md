# Comprehensions

## What is it?

Comprehensions are concise ways to create new sequences (lists, sets, dictionaries) from existing iterables. They allow you to write more readable and expressive code for transforming and filtering data.

## Examples

```python
# List comprehension
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# With condition
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# Set comprehension
unique_lengths = {len(word) for word in ["hi", "hello", "hey"]}  # {2, 3, 5}

# Dictionary comprehension
squared_map = {x: x**2 for x in range(3)}  # {0: 0, 1: 1, 2: 4}
```

## Key Points

- List, set, and dict comprehensions are more concise and often faster than loops.
- Syntax: `[expression for item in iterable if condition]` (condition is optional).
- Use comprehensions for simple transformations and filtering.
- Avoid overly complex comprehensions for readability.
- Generator expressions use `()` instead of `[]` and are memory efficient.
