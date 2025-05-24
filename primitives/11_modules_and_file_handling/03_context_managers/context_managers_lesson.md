# Context Managers

## What is it?

Context managers are a Python feature that handles setup and teardown operations automatically, typically used with the `with` statement. They ensure proper resource management (like file handles, network connections, and locks) even if errors occur. Context managers implement the `__enter__` and `__exit__` methods.

## Examples

```python
# Using a file context manager
with open("example.txt", "w") as file:
    file.write("Hello, world!")
# File is automatically closed when the block exits

# Creating a custom context manager using a class
class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        return self  # Return the context manager object
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.end = time.time()
        print(f"Elapsed time: {self.end - self.start:.6f} seconds")
        return False  # Don't suppress exceptions
        
# Using the custom context manager
with Timer() as timer:
    # Code to time goes here
    for i in range(1000000):
        pass

# Creating a context manager using contextlib
from contextlib import contextmanager

@contextmanager
def temp_file(filename):
    # Setup
    f = open(filename, "w")
    try:
        yield f  # Yield control back to the with block
    finally:
        # Teardown
        f.close()
        import os
        os.remove(filename)  # Delete the temporary file

# Using the contextlib-based context manager
with temp_file("temp.txt") as f:
    f.write("Temporary data")
# File is automatically closed and deleted

## Parenthesized Context Managers (Python 3.10+)

You can use parentheses to group multiple context managers for readability, especially with long lines.

```python
with (
    open('file1.txt') as f1,
    open('file2.txt') as f2
):
    data1 = f1.read()
    data2 = f2.read()
```

- This is equivalent to using multiple context managers in a single with statement, but is easier to read for long lists.

## Key Points

- Context managers handle resource acquisition and release.
- The `with` statement makes exception handling cleaner.
- Class-based context managers implement `__enter__` and `__exit__`.
- The `contextlib` module simplifies creating context managers with generators.
- Common uses: file handling, database connections, locks, temporary state changes.
- Ensures cleanup happens even if exceptions occur. 