# Examples and use cases for Scope and Namespaces

# --- Examples ---

def outer():
    x = 'enclosing'
    def inner():
        x = 'local'
        print(x)
    inner()
    print(x)

outer()  # Output: local\nenclosing

# --- Questions ---
# 1. What does LEGB stand for in Python's scope resolution?
# 2. How can you modify a global variable inside a function?