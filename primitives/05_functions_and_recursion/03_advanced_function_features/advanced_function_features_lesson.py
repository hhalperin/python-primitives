# Examples and use cases for Advanced Function Features

# --- Examples ---

# Variable positional arguments (*args)
def average(*args):
    if not args:
        return 0
    return sum(args) / len(args)

print(average(1, 2, 3, 4, 5))  # 3.0
print(average())               # 0

# Variable keyword arguments (**kwargs)
def create_profile(**kwargs):
    profile = {"name": "Anonymous"}
    profile.update(kwargs)
    return profile

print(create_profile(name="Bob", age=25, job="Developer"))
print(create_profile(age=30))

# Keyword-only arguments
def configure(*, host="localhost", port=8080, secure=False):
    config = f"Connecting to {host}:{port}"
    if secure:
        config += " (secure)"
    return config

print(configure(port=9000, secure=True))
# print(configure(9000))  # Would raise TypeError

# --- Questions ---
# 1. What's the difference between *args and **kwargs in a function definition?
# 2. How would you define a function where certain parameters must be specified by keyword only? 