# Pythonic Idioms and Style

## What is it?

Pythonic idioms are the preferred, idiomatic ways to accomplish common tasks in Python. These patterns leverage Python's unique features to write code that is not only functional but also clear, concise, and in harmony with the language's design philosophy. Understanding these idioms is key to writing "Pythonic" code that other Python developers can easily read and maintain.

## Examples

```python
# Duck typing - "If it walks like a duck and quacks like a duck, it's a duck"
# Instead of checking types explicitly:
def process_data(data):
    # Not Pythonic:
    if isinstance(data, list) or isinstance(data, tuple):
        for item in data:
            print(item)
    
    # Pythonic (duck typing):
    try:
        for item in data:  # If it's iterable, let's iterate!
            print(item)
    except TypeError:
        print("Data is not iterable")

# EAFP vs LBYL
# LBYL (Look Before You Leap) - Non-Pythonic
if "key" in my_dict:
    value = my_dict["key"]
else:
    value = "default"

# EAFP (Easier to Ask Forgiveness than Permission) - Pythonic
try:
    value = my_dict["key"]
except KeyError:
    value = "default"

# Idiomatic looping
colors = ["red", "green", "blue"]

# Non-Pythonic
for i in range(len(colors)):
    print(i, colors[i])

# Pythonic
for i, color in enumerate(colors):
    print(i, color)

# Non-Pythonic
i = 0
while i < len(colors):
    print(colors[i])
    i += 1

# Pythonic
for color in colors:
    print(color)

# Idiomatic dictionary handling
# Non-Pythonic
keys = list(my_dict.keys())
for key in keys:
    print(key, my_dict[key])

# Pythonic
for key, value in my_dict.items():
    print(key, value)

# List comprehensions over map/filter
# Non-Pythonic
squares = list(map(lambda x: x**2, range(10)))

# Pythonic
squares = [x**2 for x in range(10)]

# Non-Pythonic
even_squares = list(filter(lambda x: x % 2 == 0, squares))

# Pythonic
even_squares = [x for x in squares if x % 2 == 0]

# Unpacking for swapping and multiple assignment
a, b = 1, 2
a, b = b, a  # Swap values

first, *rest, last = [1, 2, 3, 4, 5]
```

## Key Points

- **Duck Typing**: Focus on what an object can do, not what it is.
- **EAFP**: Prefer try/except over checking conditions beforehand.
- **Use built-in tools**: Leverage `enumerate()`, `zip()`, `items()`, etc.
- **Avoid explicit loops** when a more idiomatic approach exists.
- **Be explicit**: Clear intent is better than implicit cleverness.
- **Embrace comprehensions** over map/filter for simple cases.
- **Use generators** for processing large datasets.
- **Follow common patterns** from the standard library.
- **Write fewer lines of code** without sacrificing readability. 