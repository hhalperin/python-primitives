# Examples and use cases for File Handling

# --- Examples ---

# Write to a file
with open('test.txt', 'w') as f:
    f.write('Test line')

# Read from a file
with open('test.txt', 'r') as f:
    print(f.read())

# --- Questions ---
# 1. What does the 'with' statement do when working with files?
# 2. How do you handle the case where a file might not exist when you try to open it?