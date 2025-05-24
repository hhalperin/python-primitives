# Examples and use cases for Simple Unit Testing

# --- Examples ---

import unittest

def multiply(a, b):
    return a * b

class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(2, 4), 8)
        self.assertEqual(multiply(-1, 5), -5)

# --- Questions ---
# 1. What is the purpose of a unit test?
# 2. How do you run all tests in a unittest.TestCase class?