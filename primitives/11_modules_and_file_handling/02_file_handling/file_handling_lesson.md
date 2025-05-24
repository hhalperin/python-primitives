# File Handling

## What is it?

File handling is the process of reading from and writing to files on disk. Python provides built-in functions like `open()`, and context managers (`with` statement) to safely work with files.

## Examples

```python
# Writing to a file
with open('example.txt', 'w') as f:
    f.write('Hello, file!')

# Reading from a file
with open('example.txt', 'r') as f:
    content = f.read()
    print(content)

# Appending to a file
with open('example.txt', 'a') as f:
    f.write('\nAnother line')
```

## Key Points

- Always close files (use `with` to do this automatically).
- Modes: 'r' (read), 'w' (write), 'a' (append), 'b' (binary).
- Reading and writing can be done line by line or all at once.
- Handle exceptions (e.g., `FileNotFoundError`) for robust code.

## Using pathlib (Python 3.4+)

The pathlib module provides an object-oriented approach to file and path operations and is recommended over os.path for new code.

```python
from pathlib import Path

p = Path('example.txt')
p.write_text('Hello, pathlib!')
print(p.read_text())

# List all .txt files in a directory
for txt_file in Path('.').glob('*.txt'):
    print(txt_file)
```

- pathlib makes file and directory operations more readable and robust.
- Use Path objects instead of string paths for most new code.
