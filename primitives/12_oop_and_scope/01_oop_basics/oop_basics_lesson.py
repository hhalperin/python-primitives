# Examples and use cases for OOP Basics

# --- Examples ---

class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print(f"Hello, my name is {self.name}.")

p = Person("Alice")
p.greet()

# --- Questions ---
# 1. The __init__ method is a special constructor method that initializes a new object when it is created. It sets up the initial state of the object by assigning values to its attributes. In the example above, __init__ takes a name parameter and assigns it to self.name.
# 2. How do you call a method on an object?