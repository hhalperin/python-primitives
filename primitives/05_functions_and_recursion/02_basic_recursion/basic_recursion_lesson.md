# Basic Recursion

## What is it?

Recursion is a programming technique where a function calls itself to solve a problem. Each recursive call should bring the problem closer to a base case, which stops the recursion. Recursion is useful for problems that can be broken down into similar subproblems, such as factorial, Fibonacci, and tree traversal.

## Examples

```python
# Factorial using recursion
def factorial(n):
    if n == 0:
        return 1  # base case
    else:
        return n * factorial(n - 1)  # recursive case

print(factorial(5))  # 120

# Fibonacci using recursion
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))  # 8
```

## Key Points

- Every recursion must have a base case to avoid infinite loops.
- Each call should reduce the problem size.
- Recursion can be less efficient than iteration for some problems (due to call stack).
- Use recursion for problems that are naturally recursive (e.g., tree/graph traversal).
