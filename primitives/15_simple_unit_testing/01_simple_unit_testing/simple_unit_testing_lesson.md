# Simple Unit Testing

## What is it?

Unit testing is the practice of writing tests for small, isolated pieces of code (units) to ensure they work as expected. Python's built-in `unittest` module makes it easy to write and run tests.

## Examples

```python
import unittest

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)
    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)

if __name__ == '__main__':
    unittest.main()
```

## Key Points

- Unit tests check that functions and classes behave as expected.
- Use `unittest` or `pytest` for writing tests.
- Good tests are isolated, repeatable, and cover edge cases.
- Run tests regularly to catch bugs early.
