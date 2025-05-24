# Built-in Functions

## What is it?

Python provides a set of built-in functions that are always available. These functions perform common tasks such as type conversion, mathematical operations, working with collections, and more. Knowing the most useful built-ins can make your code more concise and efficient.

Common built-in functions include: `len()`, `sum()`, `min()`, `max()`, `sorted()`, 
`list()`, `dict()`, `set()`, `type()`, `range()`, `abs()`, `round()`, `enumerate()`, 
`zip()`, `any()`, `all()`, `input()`, `print()`.

## Examples

```python
numbers = [3, 1, 4, 1, 5]
print(len(numbers))      # 5
print(sum(numbers))      # 14
print(min(numbers))      # 1
print(max(numbers))      # 5
print(sorted(numbers))   # [1, 1, 3, 4, 5]

s = "hello"
print(list(s))          # ['h', 'e', 'l', 'l', 'o']
print(type(s))           # <class 'str'>

for i, v in enumerate(numbers):
    print(i, v)
```

## all() and any() Functions

The `all()` and `any()` functions are powerful tools for checking conditions across iterable items:

- `all(iterable)`: Returns `True` if all elements in the iterable are truthy (or if the iterable is empty)
- `any(iterable)`: Returns `True` if at least one element in the iterable is truthy (returns `False` if the iterable is empty)

Both functions use short-circuit evaluation, meaning they stop processing as soon as they can determine the result.

### Examples of all()

```python
# All values are truthy
print(all([True, 1, "hello"]))  # True

# Not all values are truthy (0 is falsy)
print(all([True, 0, "hello"]))  # False

# Empty iterable
print(all([]))  # True (vacuously true)

# Short-circuit behavior
def check_item(item):
    print(f"Checking {item}")
    return item > 0

numbers = [5, 3, 0, 8, 1]
result = all(check_item(n) for n in numbers)
print(result)
# Output:
# Checking 5
# Checking 3
# Checking 0
# False
# (Stops after finding 0 because the result is determined)

# Practical use case: validating all conditions
def validate_user(user):
    return all([
        user.get('name', '').strip() != '',  # Name not empty
        user.get('age', 0) >= 18,            # Age at least 18
        '@' in user.get('email', '')         # Email contains @
    ])
```

### Examples of any()

```python
# At least one value is truthy
print(any([False, 0, "", "hello"]))  # True

# No truthy values
print(any([False, 0, ""]))  # False

# Empty iterable
print(any([]))  # False

# Short-circuit behavior
def is_prime(n):
    print(f"Checking if {n} is prime")
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [4, 6, 8, 7, 9]
result = any(is_prime(n) for n in numbers)
print(result)
# Output:
# Checking if 4 is prime
# Checking if 6 is prime
# Checking if 8 is prime
# Checking if 7 is prime
# True
# (Stops after finding 7 is prime because the result is determined)

# Practical use case: checking for any matching items
def has_access(user, required_roles):
    return any(role in user['roles'] for role in required_roles)
```

## Key Points

- Built-in functions are always available (no import needed).
- They work with many data types (numbers, strings, lists, etc.).
- Use `help(function_name)` or `dir(__builtins__)` to explore more built-ins.
- Mastering built-ins makes your code more Pythonic and efficient.
- `all()` and `any()` use short-circuit evaluation for efficiency.
- `all()` returns `True` for empty iterables, while `any()` returns `False`.
- These functions are excellent for writing clean, readable conditional logic.
