# 21 Copying Objects

## What is it?

Copying objects in Python means creating a new object with the same contents as an existing one. There are two main types of copies:
- **Shallow copy**: Copies the outer object, but not nested objects (references are shared).
- **Deep copy**: Copies the object and all nested objects recursively (no shared references).

## Examples

```python
import copy

# Shallow copy
original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
shallow[0][0] = 99
print(original)  # [[99, 2], [3, 4]] (inner list is shared)

# Deep copy
deep = copy.deepcopy(original)
deep[0][0] = 42
print(original)  # [[99, 2], [3, 4]] (no change)
print(deep)      # [[42, 2], [3, 4]]

# For lists, shallow copy can also be made with list() or [:]
```

## Key Points

- Use `copy.copy()` for shallow copy, `copy.deepcopy()` for deep copy.
- Shallow copy shares nested objects; deep copy does not.
- For simple lists, `list()` or slicing (`[:]`) creates a shallow copy.
- Be careful with nested (multi-level) objects—shallow copy may not be enough.
