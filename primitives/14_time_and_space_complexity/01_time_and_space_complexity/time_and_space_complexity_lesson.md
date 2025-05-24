# Time and Space Complexity

## What is it?

Time complexity measures how the runtime of an algorithm grows as the input size increases. Space complexity measures how much memory an algorithm uses as the input size increases. Big O notation (e.g., O(n), O(1)) is used to describe these complexities.

## Examples

```python
# O(1) time: constant
x = 5

# O(n) time: linear
for item in my_list:
    print(item)

# O(n^2) time: quadratic
for i in range(n):
    for j in range(n):
        print(i, j)
```

## Key Points

- Big O notation describes the upper bound of time/space usage.
- Common complexities: O(1), O(log n), O(n), O(n^2).
- Aim for lower complexity for better performance.
- Analyze both time and space for efficient code.
- Python's built-in data structures have typical complexities (e.g., list append O(1), dict lookup O(1)).
