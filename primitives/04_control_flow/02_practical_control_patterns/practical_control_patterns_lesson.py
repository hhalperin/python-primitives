# Examples and use cases for Practical Control Patterns

# --- Examples ---

# Sentinel value in a loop
numbers = []
print("Enter numbers, type 'done' to finish")

# Commented out to avoid waiting for user input:
# while True:
#     user_input = input("> ")
#     if user_input == "done":  # Sentinel value
#         break
#     numbers.append(int(user_input))
# print(f"Numbers: {numbers}")

# Chained comparison
def check_grade(score):
    if 0 <= score <= 100:
        if 90 <= score <= 100:
            return "A"
        elif 80 <= score < 90:
            return "B"
        elif 70 <= score < 80:
            return "C"
        else:
            return "D"
    else:
        return "Invalid score"

print(check_grade(85))  # B
print(check_grade(105))  # Invalid score

# Ternary expression
age = 20
status = "can vote" if age >= 18 else "cannot vote"
print(f"Person {status}")

# Loop with else clause
def search(items, target):
    for i, item in enumerate(items):
        if item == target:
            print(f"Found {target} at position {i}")
            break
    else:
        print(f"{target} not found")

search([1, 2, 3, 4], 3)  # Found 3 at position 2
search([1, 2, 3, 4], 5)  # 5 not found

# Walrus operator example (Python 3.8+)
# Simple validation
def get_positive_number():
    if (n := int(input("Enter a positive number: "))) > 0:
        return n
    return "Not positive"

# Commented out to avoid input:
# print(get_positive_number())

# --- Questions ---
# 1. What is the benefit of using a chained comparison like 18 <= age < 65 instead of age >= 18 and age < 65?
# 2. What exactly does the walrus operator (:=) do, and in what situations would you use it? 

a = 5      # 0b0101
b = 3      # 0b0011
print(a | b)  # 7 (0b0111)