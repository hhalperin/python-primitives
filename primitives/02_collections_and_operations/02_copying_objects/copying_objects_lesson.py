# Examples and use cases for Copying Objects

# --- Examples ---

import copy

# Shallow copy of a list
lst1 = [1, 2, 3]
lst2 = lst1[:]
lst2.append(4)
print('lst1:', lst1)  # [1, 2, 3]
print('lst2:', lst2)  # [1, 2, 3, 4]

# Shallow copy with nested lists
nested1 = [[1, 2], [3, 4]]
nested2 = copy.copy(nested1)
nested2[0][0] = 99
print('nested1:', nested1)  # [[99, 2], [3, 4]]
print('nested2:', nested2)  # [[99, 2], [3, 4]]

# Deep copy
nested3 = copy.deepcopy(nested1)
nested3[0][0] = 42
print('nested1:', nested1)  # [[99, 2], [3, 4]]
print('nested3:', nested3)  # [[42, 2], [3, 4]]

# --- Questions ---
# 1. What is the difference between a shallow copy and a deep copy?
# 2. How can you make a shallow copy of a list without using the copy module?