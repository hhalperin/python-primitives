# String Methods and Formatting

## What is it?

String methods are built-in functions that operate on string objects, allowing you to manipulate and analyze text. String formatting refers to ways of constructing strings with variable content, such as inserting values or controlling the appearance of output.

## Examples

```python
# Common string methods
s = "hello world"
print(s.upper())      # 'HELLO WORLD'
print(s.capitalize()) # 'Hello world'
print(s.replace('world', 'Python')) # 'hello Python'
print(s.split())      # ['hello', 'world']
print(s.startswith('he')) # True
print(s.removeprefix('he')) # 'llo world' (Python 3.9+)
print(s.removesuffix('world')) # 'hello ' (Python 3.9+)

# String formatting (f-strings, format method, % operator)
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")
print(f"{age=}")  # Shows 'age=30' (Python 3.8+)
print("My name is {} and I am {} years old.".format(name, age))
print("My name is %s and I am %d years old." % (name, age))
```

## Key Points

- Strings are immutable sequences of Unicode characters.
- Common methods: `.upper()`, `.lower()`, `.capitalize()`, `.replace()`, `.split()`, `.join()`, `.strip()`, `.startswith()`, `.endswith()`.
- F-strings (since Python 3.6) are the most modern and readable way to format strings.
- F-strings support the '=' debug specifier (Python 3.8+), e.g. f'{var=}' outputs 'var=value'.
- F-string error messages are more helpful in Python 3.12+.
- The `format()` method and `%` operator are older but still widely used.
- String formatting allows for control over number formatting, alignment, and more.
- Always use the method or formatting style that makes your code most readable.
