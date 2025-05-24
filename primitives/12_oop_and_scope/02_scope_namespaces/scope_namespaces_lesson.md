# Scope and Namespaces

## What is it?

Scope refers to the region of code where a variable is accessible. Namespaces are containers that map names to objects. Python uses LEGB (Local, Enclosing, Global, Built-in) rule to resolve variable names.

## Examples

```python
global_var = 'global'

def outer():
    enclosing_var = 'enclosing'
    def inner():
        local_var = 'local'
        print(local_var, enclosing_var, global_var)
    inner()

outer()  # Output: local enclosing global
```

## Key Points

- Local scope: inside a function.
- Enclosing scope: in nested functions.
- Global scope: at the top level of a module.
- Built-in scope: names preassigned by Python (e.g., `len`).
- Use `global` and `nonlocal` to modify variables in outer scopes (use sparingly).
