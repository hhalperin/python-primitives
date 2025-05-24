# Decorators

## What is it?

Decorators are a powerful feature in Python that allows you to modify the behavior of functions or classes without permanently modifying their source code. They wrap a function or method, adding functionality before or after the original code executes. Decorators are functions that take another function as an input and return a new function.

## Examples

```python
# Basic decorator
def simple_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@simple_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.

# Decorator with arguments
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hi(name):
    print(f"Hi, {name}!")
    return name

say_hi("Alice")
# Output:
# Hi, Alice!
# Hi, Alice!
# Hi, Alice!

# Decorator with functools.wraps to preserve metadata
from functools import wraps

def log_function_call(func):
    @wraps(func)  # Preserves original function's metadata
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@log_function_call
def add(a, b):
    """Add two numbers and return the result."""
    return a + b

result = add(3, 5)
print(add.__name__)  # 'add' (preserved by @wraps)
print(add.__doc__)   # 'Add two numbers and return the result.' (preserved)
```

## Key Points

- Decorators modify or enhance functions without changing their source code.
- Use `@decorator_name` syntax to apply a decorator to a function.
- Decorators can be stacked (multiple decorators on one function).
- Use `functools.wraps` to preserve the wrapped function's metadata.
- Common uses: logging, timing, authentication, caching, input validation.
- Decorators can take arguments and be applied to classes as well as functions.
- Understanding decorators is essential for frameworks like Flask and Django. 