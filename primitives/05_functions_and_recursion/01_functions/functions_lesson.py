# Examples and use cases for Functions

# --- Examples ---

def say_hello():
    print("Hello!")

say_hello()  # Hello!

def multiply(x, y=2):
    return x * y

print(multiply(3))    # 6
print(multiply(3, 4)) # 12

def describe_person(name, age):
    return f"{name} is {age} years old."

print(describe_person("Bob", 25))

# --- Questions ---
# 1. What is the difference between a function argument and a return value?
# 2. How do you specify a default value for a function argument in Python?