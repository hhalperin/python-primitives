# Examples and use cases for Pythonic Idioms and Style

# --- Examples ---

# Duck typing
def process_items(items):
    try:
        iterator = iter(items)  # Try to iterate
        for item in items:
            print(f"Processing {item}")
    except TypeError:
        print("Expected an iterable")

process_items([1, 2, 3])  # Works with a list
process_items((4, 5, 6))  # Works with a tuple
process_items("hello")    # Works with a string
process_items(123)        # Error: not iterable

# EAFP (Easier to Ask Forgiveness than Permission)
user_data = {"name": "Alice", "age": 30}

# LBYL style (Look Before You Leap) - less Pythonic
if "email" in user_data:
    email = user_data["email"]
else:
    email = "Not provided"

# EAFP style - more Pythonic
try:
    email = user_data["email"]
except KeyError:
    email = "Not provided"

print(f"Email: {email}")

# Pythonic looping with enumerate
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"Color {index}: {color}")

# Dictionary iteration the Pythonic way
scores = {"Alice": 95, "Bob": 87, "Charlie": 92}
for name, score in scores.items():
    print(f"{name}: {score}")

# --- Questions ---
# 1. What is the difference between "EAFP" and "LBYL" styles in Python?
# 2. Why is using enumerate() considered more Pythonic than manual index tracking in loops? 