# Type Conversion

## What is it?

Type conversion is the process of converting a value from one data type to another. In Python, this can be done explicitly (by calling a function like `int()`, `float()`, `str()`, or `list()`) or implicitly (automatically by Python in some operations).

## Examples

```python
# Explicit conversion
x = "123"
y = int(x)  # y is now an integer 123
z = float(x)  # z is now a float 123.0

# Convert number to string
n = 456
s = str(n)  # s is now "456"

# Convert list to set
lst = [1, 2, 2, 3]
st = set(lst)  # st is {1, 2, 3}

# Implicit conversion
result = 5 + 2.0  # int + float -> float (7.0)
```

## Key Points

- Use `int()`, `float()`, `str()`, `list()`, `set()`, etc. for explicit type conversion.
- Implicit conversion (type coercion) happens in some operations (e.g., int + float = float).
- Converting incompatible types (e.g., `int("abc")`) will raise a `ValueError`.
- Type conversion is useful for data processing, user input, and working with APIs.
