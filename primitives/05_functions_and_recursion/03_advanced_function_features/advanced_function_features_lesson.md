# Advanced Function Features

## What is it?

Python functions support flexible argument handling through special syntax: `*args` for variable positional arguments, `**kwargs` for variable keyword arguments, default values, and position/keyword markers. These features allow for versatile and expressive function signatures.

## Examples

```python
# *args for variable positional arguments
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3, 4))  # 10

# **kwargs for variable keyword arguments
def user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

user_info(name="Alice", age=30, city="New York")

# Positional-only and keyword-only arguments (Python 3.8+)
def calculate(a, b, /, c=None, *, d):
    # a, b are positional-only (/ marker)
    # c is regular argument with default
    # d is keyword-only (* marker)
    result = a + b
    if c:
        result += c
    return result * d

# calculate(1, 2, d=3)        # Valid
# calculate(a=1, b=2, d=3)    # Error: a, b must be positional
# calculate(1, 2, 3, d=4)     # Valid
# calculate(1, 2, d=3, c=4)   # Valid
# calculate(1, 2)             # Error: missing d

# Combined all features
def advanced_func(pos1, pos2, /, regular1=None, *args, kw_only=None, **kwargs):
    print(f"Positional-only: {pos1}, {pos2}")
    print(f"Regular: {regular1}")
    print(f"Variable positional: {args}")
    print(f"Keyword-only: {kw_only}")
    print(f"Variable keywords: {kwargs}")

advanced_func(1, 2, "reg", "arg1", "arg2", kw_only="must be named", extra1=True, extra2=False)
```

## First-Class Functions

In Python, functions are first-class objects, which means they can be:
- Assigned to variables
- Passed as arguments to other functions
- Returned from other functions
- Stored in data structures like lists or dictionaries

This enables powerful programming paradigms such as functional programming.

```python
# Assigning functions to variables
def greet(name):
    return f"Hello, {name}!"

say_hello = greet
print(say_hello("Alice"))  # "Hello, Alice!"

# Passing functions as arguments
def apply_twice(func, value):
    return func(func(value))

def double(x):
    return x * 2

print(apply_twice(double, 3))  # 12 (double applied twice: 3 -> 6 -> 12)

# Functions as return values
def create_multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

double = create_multiplier(2)
triple = create_multiplier(3)
print(double(5))  # 10
print(triple(5))  # 15

# Storing functions in data structures
function_list = [
    lambda x: x**2,
    lambda x: x*2,
    lambda x: x+10
]

for func in function_list:
    print(func(5))  # 25, 10, 15
```

## Closures

Closures are functions that "remember" the values in the enclosing scope even if they are executed outside that scope. A closure is created when a nested function references variables from its enclosing function.

```python
# Basic closure
def make_counter():
    count = 0  # This variable is "captured" by the closure
    
    def increment():
        nonlocal count  # Need nonlocal to modify the captured variable
        count += 1
        return count
        
    return increment

counter = make_counter()
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3

# Another counter doesn't share state
counter2 = make_counter()
print(counter2())  # 1 (separate counter)
print(counter())   # 4 (original counter continues)

# Function factory with parameters
def power_function(exponent):
    def power(base):
        return base ** exponent
    return power
    
square = power_function(2)
cube = power_function(3)

print(square(4))  # 16
print(cube(4))    # 64

# Common closure gotcha with loops
functions = []
for i in range(3):
    functions.append(lambda: i)  # All functions capture the same i

# All functions will use the final value of i (2)
for f in functions:
    print(f())  # 2, 2, 2

# Fix: Create a new scope with default arguments
functions_fixed = []
for i in range(3):
    functions_fixed.append(lambda i=i: i)  # Each function gets its own i

for f in functions_fixed:
    print(f())  # 0, 1, 2
```

## Key Points

- `*args` captures excess positional arguments as a tuple.
- `**kwargs` captures excess keyword arguments as a dictionary.
- Use `/` to indicate positional-only parameters (must be passed positionally).
- Use `*` to indicate keyword-only parameters (must be passed by keyword).
- Parameter order matters: positional-only, regular, *args, keyword-only, **kwargs.
- Default values help make functions more flexible.
- First-class functions can be assigned, passed, returned, and stored like any other object.
- Closures "remember" variables from their enclosing scope even when executed elsewhere.
- Use the `nonlocal` keyword to modify variables from the enclosing scope.
- Be careful with closures in loops, as they capture the variable not its value at that moment.
- These features are important for creating APIs, decorators, and adaptable functions. 