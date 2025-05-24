# Mutability vs. Immutability

## What is it?

In Python, objects are either mutable or immutable. This determines whether their contents (state) can be changed after they are created.

- **Mutable objects** can be changed in place. Examples: lists, dictionaries, sets.
- **Immutable objects** cannot be changed after creation. Examples: integers, floats, strings, tuples, frozensets.

Understanding mutability is important for writing bug-free code, especially when passing objects to functions or working with collections.

## Examples

```python
# Mutable example: list
my_list = [1, 2, 3]
my_list[0] = 99  # This works

# Immutable example: tuple
my_tuple = (1, 2, 3)
# my_tuple[0] = 99  # This would raise a TypeError

# Immutable example: string
s = "hello"
# s[0] = 'H'  # This would raise a TypeError
s = "Hello"  # You can reassign, but not change in place
```

## Key Points

- Mutability affects how objects behave when passed to functions or assigned to new variables.
- Mutable objects can be changed in place; immutable objects cannot.
- Common mutable types: list, dict, set.
- Common immutable types: int, float, str, tuple, frozenset.
- Be careful with default mutable arguments in functions (can lead to bugs).
- Use `id(obj)` to check if two variables refer to the same object in memory.
