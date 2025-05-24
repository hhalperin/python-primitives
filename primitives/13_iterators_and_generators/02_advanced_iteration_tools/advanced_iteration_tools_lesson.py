# Examples and use cases for Advanced Iteration Tools

# --- Examples ---

# itertools examples
import itertools

# Combinations - All possible ways to select k items from a collection
colors = ['red', 'blue', 'green']
for combo in itertools.combinations(colors, 2):
    print(combo)

# Permutations - All possible arrangements of items
for perm in itertools.permutations(['A', 'B', 'C'], 2):
    print(perm)

# Chain - Combine multiple iterables
numbers = list(itertools.chain([1, 2], [3, 4], [5, 6]))
print(f"Chained list: {numbers}")

# collections examples
from collections import Counter, defaultdict, deque

# Counter - Count occurrences of elements
fruits = ['apple', 'orange', 'apple', 'banana', 'apple', 'orange']
fruit_count = Counter(fruits)
print(fruit_count)
print(f"Most common fruit: {fruit_count.most_common(1)}")

# defaultdict - Dictionary with default value for missing keys
grouping = defaultdict(list)
animals = [('mammal', 'dog'), ('bird', 'sparrow'), ('mammal', 'cat'), ('fish', 'salmon')]
for category, animal in animals:
    grouping[category].append(animal)

print(dict(grouping))

# deque - Double-ended queue
tasks = deque(['task1', 'task2', 'task3'])
tasks.append('task4')         # Add to right
tasks.appendleft('task0')     # Add to left
print(tasks)
print(f"Next task: {tasks.popleft()}")  # Remove from left
print(f"Remaining tasks: {tasks}")

# --- Questions ---
# 1. What is the difference between combinations and permutations in itertools?
# 2. Why would you use a defaultdict instead of a regular dictionary?