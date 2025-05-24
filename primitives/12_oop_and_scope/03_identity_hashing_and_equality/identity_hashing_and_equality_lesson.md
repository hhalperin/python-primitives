# Identity, Hashing, and Equality

## What is it?

In Python, identity (`is`), hashing (`hash()`), and equality (`==`) are fundamental concepts for comparing and organizing objects. Understanding these concepts is crucial for dictionary and set operations, where objects must be hashable and equality is tested.

- **Identity**: Determines if two variables refer to the same object in memory (`is` operator)
- **Equality**: Determines if two objects have the same value (`==` operator)
- **Hashing**: Produces a fixed-size integer representing an object's value for efficient lookups

## Examples

```python
# Identity vs Equality
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # True - they have the same value
print(a is b)  # False - different objects in memory
print(a is c)  # True - same object in memory
print(id(a) == id(c))  # True - identical memory addresses

# Hashable objects (immutable)
d = {1: 'one', 'two': 2, (3, 4): 'tuple'}

# Unhashable objects (mutable)
try:
    d[[5, 6]] = 'list'  # TypeError - list is not hashable
except TypeError as e:
    print(e)

# Custom equality and hashing
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __eq__(self, other):
        if not isinstance(other, Person):
            return False
        return self.name == other.name and self.age == other.age
        
    def __hash__(self):
        return hash((self.name, self.age))

# Now Person objects can be dictionary keys
p1 = Person("Alice", 30)
p2 = Person("Alice", 30)
p3 = Person("Bob", 25)

print(p1 == p2)  # True - same name and age
print(p1 == p3)  # False - different name and age
print(hash(p1) == hash(p2))  # True - same hash value

people_dict = {p1: "Person 1", p3: "Person 3"}
print(people_dict[p2])  # "Person 1" - p2 is equal to p1, so it finds the same entry
```

## None and Identity Checks

`None` is a special singleton object in Python, representing the absence of a value. Since there is only one `None` object in memory, you should always use identity comparison (`is` or `is not`) rather than equality comparison (`==` or `!=`) when checking for `None`.

```python
# Correct way to check for None
def process_value(value):
    if value is None:        # Correct - identity check
        return "No value provided"
    return value.upper()

# Incorrect way
def process_value_incorrect(value):
    if value == None:        # Not recommended - equality check
        return "No value provided"
    return value.upper()

# Why it matters:
class CustomClass:
    def __eq__(self, other):
        return True  # This class equals everything!

obj = CustomClass()
print(obj == None)  # True - but obj is not None!
print(obj is None)  # False - correctly identifies obj is not None

# None is a singleton
x = None
y = None
print(x is y)  # Always True

# Common pattern in function parameters
def example_func(param=None):
    if param is None:
        param = []  # Default empty list
    param.append('item')
    return param
```

## Key Points

- `==` compares values; `is` compares identity (memory addresses).
- Only hashable objects can be used as dictionary keys or set elements.
- By default, immutable types (e.g., int, str, tuple) are hashable; mutable types (e.g., list, dict) are not.
- A proper `__hash__` method should return the same value for objects that are considered equal.
- If you implement `__eq__`, you should also implement `__hash__` to maintain consistency.
- Setting `__hash__ = None` makes a class unhashable (default for classes with mutable attributes).
- Hash values should not change during an object's lifetime.
- Always use `is None` or `is not None` when checking for None, never `== None`.
- None is a singleton, meaning there's only one None object in the entire Python interpreter. 