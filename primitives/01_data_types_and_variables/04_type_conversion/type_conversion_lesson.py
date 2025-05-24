# Examples and use cases for Type Conversion

# --- Examples ---

# Convert string to int
s = "42"
num = int(s)
print(num, type(num))  # 42 <class 'int'>

# Convert int to float
n = 7
f = float(n)
print(f, type(f))  # 7.0 <class 'float'>

# Convert list to set
lst = [1, 2, 2, 3]
st = set(lst)
print(st, type(st))  # {1, 2, 3} <class 'set'>

# Implicit conversion
result = 10 + 2.5
print(result, type(result))  # 12.5 <class 'float'>

# --- Questions ---
# 1. What happens if you try to convert the string 'hello' to an int using int('hello')?
# 2. How can you convert a float to an integer, and what happens to the value?