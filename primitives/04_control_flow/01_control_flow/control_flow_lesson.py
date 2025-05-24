# Examples and use cases for Control Flow

# --- If/elif/else ---
x = 5
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")
# Output: x is positive

# --- For loop ---
for letter in "cat":
    print(letter)
# Output:
# c
# a
# t

# --- While loop ---
n = 0
while n < 3:
    print(n)
    n += 1
# Output:
# 0
# 1
# 2

# --- break, continue, pass ---
for i in range(5):
    if i == 2:
        continue  # skip 2
    if i == 4:
        break     # stop at 4
    print(i)
# Output:
# 0
# 1
# 3

# pass is a no-op (does nothing)
if False:
    pass  # Placeholder for future code

# --- Common pattern: searching for an item ---
found = False
for num in [1, 3, 5, 7]:
    if num == 5:
        found = True
        break
if found:
    print("Found 5!")
# Output: Found 5!

# --- Question answers ---
# 1. break exits the loop entirely; continue skips to the next iteration.
# 2. Python will raise an IndentationError if you forget to indent after an if statement.