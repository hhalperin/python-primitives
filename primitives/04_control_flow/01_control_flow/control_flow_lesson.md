# 4 Control Flow

## What is it?

Control flow refers to the order in which individual statements, instructions, or function calls are executed or evaluated in a program. In Python, control flow is managed using conditional statements (like `if`), loops (`for`, `while`), and special keywords (`break`, `continue`, `pass`).

Control flow allows your program to make decisions, repeat actions, and skip code based on conditions.

## Examples

### If/Elif/Else
```python
x = 5
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")
```

### For Loop
```python
for letter in "cat":
    print(letter)
```

### While Loop
```python
n = 0
while n < 3:
    print(n)
    n += 1
```

### break, continue, pass
```python
for i in range(5):
    if i == 2:
        continue  # skip 2
    if i == 4:
        break     # stop at 4
    print(i)

# pass is a no-op (does nothing)
if False:
    pass  # Placeholder for future code
```

## Key Points

- **if/elif/else**: Used for conditional branching. Only the first true condition's block runs.
- **for loop**: Iterates over items in a sequence (like a list or string).
- **while loop**: Repeats as long as a condition is true.
- **break**: Exits the nearest enclosing loop immediately.
- **continue**: Skips the rest of the current loop iteration and moves to the next.
- **pass**: Does nothing; used as a placeholder.
- Indentation is critical in Python to define code blocks.
- Control flow is essential for writing dynamic, flexible programs.

---

### Questions
1. What is the difference between `break` and `continue` in a loop?
2. What happens if you forget to indent code after an `if` statement in Python?
