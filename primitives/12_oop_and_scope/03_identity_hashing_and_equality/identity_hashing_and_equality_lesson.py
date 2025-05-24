# Examples and use cases for Identity, Hashing, and Equality

# --- Examples ---

# Identity vs. equality
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(f"x == y: {x == y}")  # True (same values)
print(f"x is y: {x is y}")  # False (different objects)
print(f"x is z: {x is z}")  # True (same object)
print(f"id(x): {id(x)}, id(y): {id(y)}, id(z): {id(z)}")

# Hashable vs. unhashable
print(f"Hash of integer: {hash(42)}")
print(f"Hash of string: {hash('hello')}")
print(f"Hash of tuple: {hash((1, 2, 3))}")

try:
    hash([1, 2, 3])  # Will raise TypeError
except TypeError as e:
    print(f"Error: {e}")

# Custom class with __eq__ and __hash__
class Product:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return self.id == other.id
    
    def __hash__(self):
        return hash(self.id)

# Using our hashable class
inventory = {}
p1 = Product(1001, "Laptop")
p2 = Product(1001, "Notebook")  # Same ID but different name
inventory[p1] = 10

print(f"p1 == p2: {p1 == p2}")  # True (same ID)
print(f"p1 is p2: {p1 is p2}")  # False (different objects)
print(f"hash(p1) == hash(p2): {hash(p1) == hash(p2)}")  # True (same hash)
print(f"Inventory has p2: {p2 in inventory}")  # True (finds p1 entry)

# --- Questions ---
# 1. Why can lists not be used as dictionary keys while tuples can?
# 2. What happens if you define __eq__ in a class but don't define __hash__? 