# Common Pitfalls

## What is it?

Common pitfalls are mistakes or misunderstandings that often trip up Python programmers, especially beginners. Being aware of these can help you write more reliable and bug-free code.

## Examples

```python
# Mutable default arguments
def append_to_list(value, my_list=[]):
    my_list.append(value)
    return my_list
# This can lead to unexpected results!

# Integer division in Python 2 vs 3
print(3 / 2)  # 1.5 in Python 3, 1 in Python 2

# Variable scope in loops
funcs = []
for i in range(3):
    funcs.append(lambda: i)
print([f() for f in funcs])  # [2, 2, 2] (not [0, 1, 2])
```

## Key Points

- Avoid using mutable default arguments in functions.
- Be aware of integer division differences between Python 2 and 3.
- Understand variable scope and late binding in closures/lambdas.
- Watch out for off-by-one errors in loops and slices.
- Test your code and read error messages carefully.
