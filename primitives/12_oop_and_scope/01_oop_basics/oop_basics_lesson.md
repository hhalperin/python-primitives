# OOP Basics

## What is it?

Object-Oriented Programming (OOP) is a programming paradigm based on the concept of objects, which contain data (attributes) and code (methods). OOP helps organize code, promote reuse, and model real-world entities.

## Examples

```python
class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        print(f"{self.name} says woof!")

my_dog = Dog("Fido")
my_dog.bark()  # Fido says woof!
```

## Key Points

- Classes define blueprints for objects; objects are instances of classes.
- Use `self` to refer to instance attributes and methods.
- The `__init__` method initializes new objects.
- OOP supports encapsulation, inheritance, and polymorphism.
- Use OOP to model complex systems and promote code reuse.

## Dataclasses (Python 3.7+)

Dataclasses are a decorator and module that make it easier to create classes for storing data. They automatically generate __init__, __repr__, __eq__, and other methods.

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p1 = Point(1, 2)
print(p1)  # Point(x=1, y=2)
```

- Use dataclasses for simple classes that mainly store data.
- You can add default values, type annotations, and more.
- Dataclasses are mutable by default, but you can make them immutable with `frozen=True`.
