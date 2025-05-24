# Data Types

## What is it?

Data types are the basic building blocks of any programming language. In Python, a data type defines what kind of value a variable can hold and what operations can be performed on it. Understanding data types is fundamental to writing correct and efficient code.

The most common built-in data types in Python are:
- **int**: Integer numbers (e.g., 5, -3, 0)
- **float**: Floating-point (decimal) numbers (e.g., 3.14, -0.001)
- **bool**: Boolean values (`True` or `False`)
- **str**: Strings (text, e.g., "hello", 'Python')

## Examples

```python
x = 5           # int
pi = 3.14      # float
is_valid = True  # bool
name = "Alice"   # str
```

You can check the type of a variable using the `type()` function:

```python
print(type(x))      # <class 'int'>
print(type(pi))     # <class 'float'>
print(type(is_valid)) # <class 'bool'>
print(type(name))   # <class 'str'>
```

## Truthy and Falsy Values

In Python, any object can be tested for truth value in boolean contexts such as `if` statements or `while` loops. This is known as "truthiness."

### Falsy Values

The following values are considered `False` in boolean contexts:
- `False`: Boolean false
- `None`: Python's null value
- `0`: Zero (integer)
- `0.0`: Zero (float)
- `''` or `""`: Empty string
- `[]`: Empty list
- `()`: Empty tuple
- `{}`: Empty dictionary
- `set()`: Empty set

### Truthy Values

Everything else is considered `True`, including:
- Non-zero numbers
- Non-empty strings, lists, dictionaries, etc.
- The boolean `True`
- Custom objects (unless `__bool__` or `__len__` is implemented to return `False`/`0`)

### Examples

```python
# Using truthiness in conditionals
name = ""
if name:  # Empty string is falsy
    print("Hello,", name)
else:
    print("Name is empty")  # This will be executed

numbers = [1, 2, 3]
if numbers:  # Non-empty list is truthy
    print("List has items")  # This will be executed

# Converting to explicit boolean with bool()
print(bool(0))      # False
print(bool(42))     # True
print(bool(""))     # False
print(bool("text")) # True
print(bool([]))     # False
print(bool([1, 2])) # True
```

## Key Points

- Python is dynamically typed: you don't need to declare a variable's type explicitly.
- Strings are immutable (cannot be changed in place).
- Integers and floats support arithmetic operations.
- Booleans are a subtype of integers (`True` is 1, `False` is 0).
- Use `type()` to check a variable's data type.
- Understanding data types helps prevent bugs and write efficient code.
- In boolean contexts, Python automatically evaluates the "truthiness" of objects.
- Use the `bool()` function to explicitly convert a value to a boolean.

## Type Annotations and Modern Type Hinting (Python 3.10+)

Python supports type annotations to help with code clarity and static analysis. Modern Python allows:
- Using `|` for type unions (e.g., `int | None`)
- Using built-in collection types with brackets (e.g., `list[int]`)
- The `Self` type for methods returning their own class (Python 3.11+)

```python
# Function with type annotations

def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(x: int | float, y: int | float) -> int | float:
    return x + y

from typing import Self
class Example:
    def set_value(self, value: int) -> Self:
        self.value = value
        return self
```

- Type annotations are optional and not enforced at runtime.
- Use them for better code documentation and editor support.
