# Examples and use cases for Decorators

# --- Examples ---

# Simple decorator without arguments
def timer(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.6f} seconds to run")
        return result
    return wrapper

@timer
def slow_function():
    import time
    time.sleep(0.1)
    return "Function completed"

print(slow_function())

# Decorator with arguments
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("World")

# Using functool.wraps to preserve metadata
from functools import wraps

def debugger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Debug: {func.__name__}({args}, {kwargs}) = {result}")
        return result
    return wrapper

@debugger
def multiply(a, b):
    """Multiply two numbers."""
    return a * b

print(multiply(4, 5))
print(f"Function name: {multiply.__name__}")
print(f"Docstring: {multiply.__doc__}")

# --- Questions ---
# 1. What is the main purpose of using decorator functions in Python?
# 2. Why should you use functools.wraps when creating decorators? 