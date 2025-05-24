# Slicing

## What is it?

Slicing is a way to extract a portion (subsequence) of a sequence type (like a list, tuple, or string) using a special syntax: `sequence[start:stop:step]`. Slicing is a powerful tool for working with collections in Python.

## Examples

```python
lst = [0, 1, 2, 3, 4, 5]
print(lst[1:4])    # [1, 2, 3] (from index 1 up to, but not including, 4)
print(lst[:3])     # [0, 1, 2] (from start up to index 3)
print(lst[3:])     # [3, 4, 5] (from index 3 to end)
print(lst[::2])    # [0, 2, 4] (every second element)
print(lst[::-1])   # [5, 4, 3, 2, 1, 0] (reversed)

s = "Python"
print(s[1:4])      # "yth"
```

## Key Points

- Slicing works on lists, tuples, strings, and other sequence types.
- The `start` index is inclusive, `stop` is exclusive.
- Omitting `start` or `stop` uses the beginning or end of the sequence.
- Negative indices count from the end.
- Slicing does not modify the original sequence; it returns a new one.
