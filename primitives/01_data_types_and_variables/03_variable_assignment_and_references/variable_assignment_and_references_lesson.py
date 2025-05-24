# Examples and use cases for Variable Assignment and References

# --- Examples ---

# Assignment creates a reference, not a copy
x = [1, 2, 3]
y = x
print('x:', x)
print('y:', y)
y.append(4)
print('After y.append(4):')
print('x:', x)  # [1, 2, 3, 4]
print('y:', y)  # [1, 2, 3, 4]

# Copying a list
a = [10, 20]
b = a.copy()
b.append(30)
print('a:', a)  # [10, 20]
print('b:', b)  # [10, 20, 30]

# --- Questions ---
# 1. What will be the output of the following code?
#    a = [1, 2, 3]
#    b = a
#    b[0] = 99
#    print(a)
#
# 2. How can you check if two variables refer to the same object in memory?