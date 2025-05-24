# Collections

## What is it?

Collections are data structures that can store multiple values in a single variable. Python provides several built-in collection types, each with different properties and use cases:
- **list**: Ordered, mutable, allows duplicates
- **tuple**: Ordered, immutable, allows duplicates
- **set**: Unordered, mutable, unique elements only
- **dict**: Unordered (ordered as of Python 3.7+), mutable, key-value pairs

## Examples

```python
# List
fruits = ["apple", "banana", "cherry"]

# Tuple
dimensions = (1920, 1080)

# Set
unique_numbers = {1, 2, 3, 2}

# Dictionary
person = {"name": "Alice", "age": 30}
```

## Key Points

- Lists and tuples are indexed (access by position), sets and dicts are not.
- Lists and sets are mutable; tuples and frozensets are immutable.
- Sets and dicts do not allow duplicate keys/elements.
- Use lists for ordered, changeable collections; sets for unique items; dicts for key-value mapping.
