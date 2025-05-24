# Iterators and Generators

## What is it?

Iterators are objects that allow you to traverse through all the elements of a collection, one at a time. Generators are a special type of iterator created with functions and the `yield` keyword, allowing you to produce a sequence of values lazily (on demand).

## Examples

```python
# Iterator from a list
nums = [1, 2, 3]
iterator = iter(nums)
print(next(iterator))  # 1
print(next(iterator))  # 2

# Generator function
def countdown(n):
    while n > 0:
        yield n
        n -= 1
for num in countdown(3):
    print(num)  # 3 2 1
```

## Lazy Evaluation with Generators

One of the most powerful features of generators is lazy evaluation. This means values are generated only when needed, not all at once. This provides significant memory efficiency for large datasets and potentially infinite sequences.

```python
# Memory comparison: list vs generator
import sys

# List holds all values in memory at once
def get_squares_list(n):
    return [i**2 for i in range(n)]

# Generator calculates values on demand
def get_squares_generator(n):
    for i in range(n):
        yield i**2

# For small n, the difference might be negligible
small_n = 10
small_list = get_squares_list(small_n)
small_gen = get_squares_generator(small_n)

# For large n, the difference is substantial
large_n = 1000000
# This allocates memory for 1 million items
large_list = get_squares_list(large_n)  
# This only creates a generator object, not the actual values
large_gen = get_squares_generator(large_n)

# Memory usage comparison
list_size = sys.getsizeof(large_list)
gen_size = sys.getsizeof(large_gen)

print(f"List size: {list_size} bytes")         # Much larger
print(f"Generator size: {gen_size} bytes")     # Very small

# Infinite sequence with generators (not possible with lists)
def infinite_counter():
    count = 0
    while True:
        yield count
        count += 1

# We can take just what we need
counter = infinite_counter()
for _ in range(5):
    print(next(counter))  # 0, 1, 2, 3, 4
```

## zip() and enumerate() Functions

These two built-in functions are essential for Pythonic iteration.

### enumerate()

`enumerate()` adds a counter to an iterable, returning pairs of (index, value). This eliminates the need for manually tracking indices.

```python
# Non-Pythonic way (avoid this)
fruits = ['apple', 'banana', 'cherry']
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# Pythonic way with enumerate()
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# You can also specify a starting index
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}: {fruit}")  # 1: apple, 2: banana, 3: cherry
```

### zip()

`zip()` combines multiple iterables into a single iterator of tuples. This is useful for parallel iteration.

```python
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
cities = ['New York', 'Boston', 'Chicago']

# Iterate over multiple sequences at once
for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old and lives in {city}")

# Create a dictionary from two sequences
name_to_age = dict(zip(names, ages))
print(name_to_age)  # {'Alice': 25, 'Bob': 30, 'Charlie': 35}

# zip() stops at the shortest sequence
shortened = [1, 2]
for n, a in zip(names, shortened):
    print(n, a)  # Only prints: Alice 1, Bob 2

# To include all elements, use itertools.zip_longest
import itertools
for name, num in itertools.zip_longest(names, shortened, fillvalue='N/A'):
    print(name, num)  # Prints: Alice 1, Bob 2, Charlie N/A
```

## Key Points

- Iterators implement `__iter__()` and `__next__()` methods.
- Use `iter()` to get an iterator, `next()` to get the next value.
- Generators use `yield` and are memory efficient for large data.
- Generator expressions are like comprehensions but use `()`.
- Lazy evaluation means values are generated only when needed, saving memory.
- Use generators for large or infinite sequences where lists would be impractical.
- `enumerate()` provides indices alongside values, eliminating manual index tracking.
- `zip()` enables parallel iteration over multiple sequences.
- Use iterators and generators for efficient looping and data processing.
