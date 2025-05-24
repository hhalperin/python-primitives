# Functional Programming

## What is it?

Functional programming is a programming paradigm where computation is treated as the evaluation of mathematical functions. It emphasizes immutability, first-class functions, and avoiding side effects. In Python, this often means using functions like `map`, `filter`, `reduce`, and `lambda` expressions.

## Examples

```python
# Using map to square numbers
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, nums))  # [1, 4, 9, 16]

# Using filter to get even numbers
evens = list(filter(lambda x: x % 2 == 0, nums))  # [2, 4]

# Using reduce to compute a product
from functools import reduce
product = reduce(lambda x, y: x * y, nums)  # 24
```

## Key Points

- Functions are first-class objects: they can be passed as arguments, returned, and assigned.
- `map`, `filter`, and `reduce` apply functions to sequences.
- `lambda` creates small anonymous functions.
- Functional programming encourages immutability and statelessness.
- Use functional tools for concise, expressive code, but avoid overusing them if it hurts readability.
