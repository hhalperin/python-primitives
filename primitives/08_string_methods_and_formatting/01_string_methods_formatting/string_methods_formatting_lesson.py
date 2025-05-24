# Examples and use cases for String Methods and Formatting

# --- Examples ---

s = "  python interview prep  "
print(s.strip())            # Remove leading/trailing whitespace
print(s.upper())            # 'PYTHON INTERVIEW PREP'
print(s.replace("prep", "guide")) # '  python interview guide  '

# String formatting
name = "Bob"
score = 95.6789
print(f"{name} scored {score:.2f} on the test.")  # 'Bob scored 95.68 on the test.'
print("{} scored {:.1f} on the test.".format(name, score))

# --- Questions ---
# 1. What is the difference between s.upper() and s.capitalize()?
# 2. Write a line of code that joins the list ['a', 'b', 'c'] into a single string separated by dashes ('-').