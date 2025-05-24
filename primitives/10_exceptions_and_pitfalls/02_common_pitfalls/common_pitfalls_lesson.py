# Examples and use cases for Common Pitfalls

# --- Examples ---

def add_item(item, my_list=[]):
    my_list.append(item)
    return my_list

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2] (unexpected!)

# --- Questions ---
# 1. Why is it bad to use a mutable default argument like a list in a function definition?
# 2. What will this print and why?
#    funcs = []
#    for i in range(3):
#        funcs.append(lambda: i)
#    print([f() for f in funcs])