# Advanced Iteration Tools

## What is it?

Python's standard library provides powerful modules for advanced iteration:
- The `itertools` module offers functions for efficient looping through iterables, permutations, combinations, and other operations.
- The `collections` module provides specialized container datatypes that enhance the standard dict, list, and tuple.

These tools can make your code more efficient, elegant, and Pythonic when dealing with complex iteration and data processing.

## Examples

```python
# itertools examples
import itertools

# Infinite iterators
for i in itertools.count(10, 2):  # Start at 10, increment by 2
    print(i)
    if i > 20:
        break  # Output: 10, 12, 14, 16, 18, 20, 22

# Combinatorial generators
print(list(itertools.combinations([1, 2, 3, 4], 2)))
# [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

print(list(itertools.permutations([1, 2, 3], 2)))
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# Joining iterables
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# Chain multiple iterables
numbers = list(itertools.chain([1, 2], [3, 4, 5], [6]))
print(numbers)  # [1, 2, 3, 4, 5, 6]

# Group consecutive items
data = [1, 1, 1, 2, 2, 3, 3, 3, 1]
for key, group in itertools.groupby(data):
    print(key, list(group))
# 1 [1, 1, 1]
# 2 [2, 2]
# 3 [3, 3, 3]
# 1 [1]

# collections examples
from collections import Counter, defaultdict, deque

# Counter
word_counts = Counter("mississippi")
print(word_counts)  # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
print(word_counts.most_common(2))  # [('i', 4), ('s', 4)]

# defaultdict
word_categories = defaultdict(list)
word_categories['fruit'].append('apple')  # No need to check if 'fruit' exists
word_categories['fruit'].append('banana')
print(dict(word_categories))  # {'fruit': ['apple', 'banana']}

# deque (efficient stack and queue)
queue = deque(['a', 'b', 'c'])
queue.append('d')        # add to right end
queue.appendleft('e')    # add to left end
print(queue)             # deque(['e', 'a', 'b', 'c', 'd'])
print(queue.pop())       # 'd'
print(queue.popleft())   # 'e'
print(queue)             # deque(['a', 'b', 'c'])
```

## Key Points

- `itertools` provides memory-efficient, fast tools for complex iteration tasks.
- Common `itertools` functions: `count`, `cycle`, `combinations`, `permutations`, `chain`, `groupby`.
- `collections` provides specialized container data types beyond the standard list, tuple, and dict.
- Common `collections` types: `Counter` (frequency counting), `defaultdict` (dict with default values), `deque` (double-ended queue).
- These tools are essential for efficient data processing, algorithm implementation, and writing idiomatic Python.
- Using these tools can reduce code complexity and improve performance.