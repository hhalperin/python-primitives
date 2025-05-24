# Examples and use cases for Exception Handling

# --- Examples ---

try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ValueError:
    print("That was not a valid integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("Done with exception handling example.")

# --- Questions ---
# 1. What is the purpose of the finally block in exception handling?
# 2. How do you raise a custom exception in Python?