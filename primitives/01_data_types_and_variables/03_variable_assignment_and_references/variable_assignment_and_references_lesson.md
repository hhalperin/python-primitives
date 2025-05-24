# Variable Assignment and References

## What is it?

In Python, variables are names that refer to objects in memory. Assignment does not copy the object, but creates a new reference to the same object. Understanding how assignment and references work is crucial for avoiding bugs, especially with mutable objects.

## Examples

```python
# Simple assignment
x = [1, 2, 3]
y = x  # y refers to the same list as x

y.append(4)
print(x)  # [1, 2, 3, 4] (x and y refer to the same object)

# To create a copy:
z = x.copy()  # or list(x)
z.append(5)
print(x)  # [1, 2, 3, 4]
print(z)  # [1, 2, 3, 4, 5]
```

## Key Points

- Assignment in Python binds a name to an object, not the value itself.
- Multiple variables can refer to the same object (aliasing).
- Changes to a mutable object via one reference affect all references.
- Use `.copy()`, `list()`, or slicing (`[:]`) to create a shallow copy of a list.
- Use `id(obj)` to check if two variables refer to the same object.
