# Examples and use cases for Context Managers

# --- Examples ---

# Basic file context manager
with open("temp_example.txt", "w") as f:
    f.write("This is a temporary file")
# File is automatically closed outside the with block

# Creating a simple context manager class
class Indenter:
    def __init__(self):
        self.level = 0
        
    def __enter__(self):
        self.level += 1
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1
        
    def print(self, text):
        print(' ' * self.level + text)

# Using our custom context manager
with Indenter() as indent:
    indent.print("First level")
    with indent:
        indent.print("Second level")
        with indent:
            indent.print("Third level")
    indent.print("Back to first level")

# Context manager using contextlib
from contextlib import contextmanager

@contextmanager
def suppress_errors():
    try:
        yield
    except Exception as e:
        print(f"Error suppressed: {e}")

# Using the error suppression context manager
with suppress_errors():
    print(1 / 0)  # This would normally raise a ZeroDivisionError

# --- Questions ---
# 1. What are the two special methods that a class must implement to be used as a context manager?
# 2. How does a context manager help with resource management compared to manual try/finally blocks? 