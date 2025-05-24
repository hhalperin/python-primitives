# Exception Handling

## What is it?

Exception handling is a way to gracefully handle errors and unexpected events in your code. In Python, this is done using `try`, `except`, `else`, and `finally` blocks. Proper exception handling prevents your program from crashing and allows you to manage error situations.

## Examples

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print("Division successful.")
finally:
    print("This always runs.")

# Raising your own exception
if not isinstance(result, int):
    raise TypeError("Result must be an integer")
```

## Custom Exceptions

Creating custom exception classes helps make your code more readable and allows for more specific error handling. Custom exceptions should inherit from built-in exceptions, typically `Exception` or a more specific one.

```python
# Define a custom exception
class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds available balance."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.deficit = amount - balance
        message = f"Cannot withdraw ${amount}. Balance is ${balance}, deficit: ${self.deficit}"
        super().__init__(message)

# Using the custom exception
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return amount

# Handling the custom exception
account = BankAccount(100)
try:
    account.withdraw(150)
except InsufficientFundsError as e:
    print(f"Error: {e}")
    print(f"You need ${e.deficit} more to complete this transaction.")

# You can also create a hierarchy of custom exceptions
class TransactionError(Exception):
    """Base class for transaction exceptions."""
    pass

class InsufficientFundsError(TransactionError):
    """Insufficient funds for transaction."""
    pass

class CardDeclinedError(TransactionError):
    """Card was declined."""
    pass

# This allows catching categories of errors
try:
    # Some transaction code...
    pass
except TransactionError as e:
    # Handles any type of transaction error
    print(f"Transaction failed: {e}")
```

## Fail-Fast Input Validation

Validating inputs early in your functions (the "fail-fast" approach) creates more reliable code and provides clearer error messages. This is a common practice in professional code.

```python
def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    # Validate input early
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    
    if not isinstance(numbers, (list, tuple)):
        raise TypeError(f"Expected a list or tuple, got {type(numbers).__name__}")
    
    # Check that all elements are numeric
    for i, num in enumerate(numbers):
        if not isinstance(num, (int, float)):
            raise TypeError(f"Element at index {i} is not a number: {num}")
    
    # After validation, proceed with the calculation
    return sum(numbers) / len(numbers)

# Another example: User registration function
def register_user(username, email, password):
    """Register a new user with validation."""
    # Validate username
    if not username or not isinstance(username, str):
        raise ValueError("Username must be a non-empty string")
    
    if len(username) < 4:
        raise ValueError("Username must be at least 4 characters long")
    
    # Validate email
    if not '@' in email or not '.' in email:
        raise ValueError("Invalid email format")
    
    # Validate password
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long")
    
    # If all validations pass, register the user
    print(f"User {username} registered successfully")
    return True
```

## Exception Groups and except* (Python 3.11+)

Python 3.11 introduced ExceptionGroup and the except* syntax, which allow you to handle multiple exceptions in parallel, especially useful for concurrent code (e.g., asyncio, threading).

```python
try:
    raise ExceptionGroup("multiple errors", [ValueError("bad value"), TypeError("bad type")])
except* ValueError as eg:
    print("Caught ValueError(s):", eg)
except* TypeError as eg:
    print("Caught TypeError(s):", eg)
```

- ExceptionGroup lets you raise and handle multiple exceptions at once.
- except* is used to catch exceptions from ExceptionGroup.
- This is especially useful in concurrent code (asyncio, threads, etc.).

## Key Points

- Use `try`/`except` to catch and handle exceptions.
- `else` runs if no exception occurs; `finally` always runs.
- Catch specific exceptions (e.g., `ValueError`) rather than using a bare `except`.
- Use `raise` to throw your own exceptions.
- Create custom exception classes by inheriting from `Exception`.
- Include relevant data in custom exceptions for better error handling.
- Validate inputs early in functions (fail-fast) for reliable code.
- Good exception handling makes your code robust and user-friendly.
