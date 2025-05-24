# Input/Output

## What is it?

Input/Output (I/O) in Python refers to reading data from the user or external sources (input) and displaying data to the user or writing to external destinations (output). The most common functions for I/O are `input()` for reading user input and `print()` for displaying output.

## Examples

```python
# Output
print("Hello, world!")

# Input (from user)
name = input("What is your name? ")
print("Hello,", name)

# Output with formatting
age = 25
print(f"I am {age} years old.")

# Multiple arguments in print
print("A", "B", "C", sep="-")  # A-B-C
```

## Key Points

- `input()` always returns a string; convert to int/float if needed.
- `print()` can take multiple arguments and supports formatting (f-strings, .format()).
- Use `end` and `sep` parameters in `print()` to control output formatting.
- For file I/O, use `open()`, `read()`, `write()`, and context managers (`with`).
