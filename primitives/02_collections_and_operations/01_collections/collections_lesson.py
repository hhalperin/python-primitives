# Examples and use cases for Collections

# --- Examples ---

# List
colors = ["red", "green", "blue"]
print(colors[1])  # green
colors.append("yellow")
print(colors)  # ['red', 'green', 'blue', 'yellow']

# Tuple
point = (10, 20)
print(point[0])  # 10
# point[0] = 5  # This would raise a TypeError

# Set
nums = {1, 2, 2, 3}
print(nums)  # {1, 2, 3}
nums.add(4)
print(nums)  # {1, 2, 3, 4}

# Dictionary
d = {"a": 1, "b": 2}
print(d["a"])  # 1
d["c"] = 3
print(d)  # {'a': 1, 'b': 2, 'c': 3}

# --- Questions ---
# 1. What is the difference between a list and a tuple?
# 2. How do you check if a key exists in a dictionary?