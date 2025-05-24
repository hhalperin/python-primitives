# Practical Control Patterns

## What is it?

Practical control patterns are idiomatic Python constructs that provide clean, efficient solutions to common control flow challenges. These include sentinel values, loop control patterns, chained comparisons, ternary expressions, and the walrus operator. These patterns help make your code more readable and maintainable.

## Examples

```python
# Sentinel values and loop patterns
def read_until_empty():
    results = []
    while True:
        line = input("Enter a value (or empty to stop): ")
        if not line:  # Empty string as sentinel
            break
        results.append(line)
    return results

# The while/else pattern (rarely seen but useful)
def find_item(items, target):
    i = 0
    while i < len(items):
        if items[i] == target:
            print(f"Found {target} at position {i}")
            break
        i += 1
    else:  # Executes if the loop completes without a break
        print(f"{target} not found")

# Chained comparisons
age = 25
if 18 <= age < 65:  # Cleaner than: if age >= 18 and age < 65
    print("Working age")

# Ternary expression (conditional expression)
status = "adult" if age >= 18 else "minor"
print(status)

# Walrus operator (:=) - Python 3.8+
# Without walrus operator:
data = get_data()
if data:
    process(data)

# With walrus operator:
if data := get_data():
    process(data)

# Loop with the walrus operator
while chunk := file.read(8192):
    process(chunk)

# The switch/case alternative (Python 3.10+)
# Pattern matching is now robust and supports many advanced patterns in Python 3.12+
def describe(obj):
    match obj:
        case [x, y]:
            return f"A 2-item sequence: {x}, {y}"
        case {"name": name, "age": age}:
            return f"A dict with name={name} and age={age}"
        case int() | float() as number if number > 0:
            return f"A positive number: {number}"
        case str() as s:
            return f"A string: {s}"
        case _:
            return "Something else"

def get_day_type(day):
    match day.lower():
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            return "Weekday"
        case "saturday" | "sunday":
            return "Weekend"
        case _:
            return "Invalid day"
```

## Key Points

- Sentinel values (like `None`, empty string, or -1) signal the end of a loop or process.
- Chained comparisons (`a < b < c`) are cleaner than `a < b and b < c`.
- The ternary expression (`x if condition else y`) is a concise conditional assignment.
- The walrus operator (`:=`) assigns and evaluates in one expression, reducing repetition.
- `while/else` and `for/else` run the `else` block only if the loop completes without a `break`.
- `match/case` (Python 3.10+) provides powerful pattern matching, including sequence, mapping, class, OR-patterns, wildcards, and guards (Python 3.12+ is robust).
- These patterns are often used in real-world code and technical interviews. 