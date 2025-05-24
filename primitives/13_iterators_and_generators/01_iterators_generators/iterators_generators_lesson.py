# Examples and use cases for Iterators and Generators

# --- Examples ---

# Iterator example
my_list = [10, 20, 30]
my_iter = iter(my_list)
print(next(my_iter))
print(next(my_iter))

# Generator example
def simple_gen():
    yield 'A'
    yield 'B'
for val in simple_gen():
    print(val)

# --- Questions ---
# 1. An iterator is an object that implements the iterator protocol (__iter__ and __next__ methods) and 
# allows you to traverse through a collection one element at a time. A generator is a special type of iterator
#  created using functions with the yield keyword, which automatically implements the iterator protocol and provides a 
# more convenient way to create iterators. Generators are particularly useful for creating lazy sequences that generate values on demand.

# 2. Generator expressions are similar to list comprehensions but use parentheses instead of square brackets. 
# They create generator objects that yield values one at a time. For example: (x**2 for x in range(10)) creates a generator 
# that yields squares of numbers from 0 to 9.