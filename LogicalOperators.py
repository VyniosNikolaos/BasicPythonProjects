# NOT operator (not)
a = True
b = False
print(f"not {a}: {not a}")
print(f"not {b}: {not b}")

# Combining logical operators
x = 5
y = 10
z = 5
result = (x < y or y > z) and not (x == z)
print(f"(x < y or y > z) and not (x == z): {result}")

# Short-circuit evaluation
def true_func():
    print("This function returns True")
    return True

def false_func():
    print("This function returns False")
    return False

# AND short-circuit (second part not evaluated if first is False)
print("AND short-circuit:")
result = false_func() and true_func()
print(f"Result: {result}")

# OR short-circuit (second part not evaluated if first is True)
print("\nOR short-circuit:")
result = true_func() or false_func()
print(f"Result: {result}")

# Using 'and' and 'or' with non-boolean values
print(f"\n0 and 1: {0 and 1}")  # Returns 0 (first falsy value)
print(f"1 and 2: {1 and 2}")  # Returns 2 (last truthy value)
print(f"0 or 1: {0 or 1}")    # Returns 1 (first truthy value)
print(f"1 or 2: {1 or 2}")    # Returns 1 (first truthy value)