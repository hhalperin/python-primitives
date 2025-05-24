# Functions

## What is it?

A function is a reusable block of code that performs a specific task. Functions help organize code, avoid repetition, and make programs easier to read and maintain. In Python, functions are defined using the `def` keyword.

Functions can take arguments (inputs), return values (outputs), and have optional default arguments and keyword arguments.

## Examples

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Hello, Alice!

# Function with default argument
def power(base, exponent=2):
    return base ** exponent

print(power(3))      # 9
print(power(3, 3))   # 27

# Function with multiple arguments
def add(a, b):
    return a + b

print(add(2, 5))     # 7
```

## Key Points

- Define a function with `def` and call it by name.
- Use `return` to send a value back to the caller.
- Arguments can have default values.
- Functions can take any number of arguments (use `*args`, `**kwargs`).
- Functions help break code into logical, reusable pieces.
