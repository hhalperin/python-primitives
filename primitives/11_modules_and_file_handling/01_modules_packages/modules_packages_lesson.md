# Modules and Packages

## What is it?

A module is a file containing Python code (functions, classes, variables) that can be imported and reused. A package is a collection of modules in a directory with an `__init__.py` file. Using modules and packages helps organize code and promote reuse.

## Examples

```python
# my_module.py
def greet(name):
    return f"Hello, {name}!"

# main.py
import my_module
print(my_module.greet("Alice"))

# Importing from a package
from my_package import my_module
```

## The `__name__ == "__main__"` Pattern

When a Python file is run directly, its `__name__` variable is set to `"__main__"`. When it's imported as a module, `__name__` is set to the module's name. This allows you to create code that can be both imported and run directly.

```python
# example.py
def useful_function():
    return "I am a useful function!"

# This code only runs when the file is executed directly
if __name__ == "__main__":
    print("Running as a script!")
    print(useful_function())
    # You can put tests, examples, or script behavior here
```

If you run `python example.py`, you'll see both print statements. If you `import example` in another file, only the function definition will be executed, not the code inside the `if` block.

### Benefits of the `__name__ == "__main__"` Pattern:

1. **Reusability**: Files can be both imported as modules and run as scripts.
2. **Testing**: You can include test code that only runs when the file is executed directly.
3. **Demonstration**: You can include example usage that only runs when executed directly.
4. **Separation of concerns**: Clearly separates importable code from execution code.

```python
# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == "__main__":
    # This code demonstrates the module's functionality
    # but won't run when the module is imported
    print(f"10 + 5 = {add(10, 5)}")
    print(f"10 - 5 = {subtract(10, 5)}")
    
    # You could also include tests here
    assert add(2, 3) == 5, "Addition test failed"
    assert subtract(5, 2) == 3, "Subtraction test failed"
    print("All tests passed!")
```

## Key Points

- Use `import` to bring in modules or functions.
- Standard library modules (e.g., `math`, `os`, `sys`) provide lots of functionality.
- Packages are directories with an `__init__.py` file.
- Use modules and packages to keep code organized and maintainable.
- The `__name__ == "__main__"` pattern allows files to serve as both modules and standalone scripts.
- Always use this pattern for code that should only run when a file is executed directly.
