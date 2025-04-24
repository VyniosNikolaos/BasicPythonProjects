# Equal to (==)
a = 5
b = 5
print(f"{a} == {b}: {a == b}")

# Not equal to (!=)
c = 7
print(f"{a} != {c}: {a != c}")

# Greater than (>)
print(f"{c} > {a}: {c > a}")

# Less than (<)
print(f"{a} < {c}: {a < c}")

# Greater than or equal to (>=)
d = 5
print(f"{a} >= {d}: {a >= d}")
print(f"{c} >= {a}: {c >= a}")

# Less than or equal to (<=)
print(f"{a} <= {d}: {a <= d}")
print(f"{a} <= {c}: {a <= c}")

# Comparing different types
num = 5
text = "5"
print(f"{num} == '{text}': {num == text}")  # This will be False

# Comparing strings (lexicographical order)
str1 = "apple"
str2 = "banana"
print(f"'{str1}' < '{str2}': {str1 < str2}")

# Chained comparisons
x = 10
print(f"5 < {x} < 15: {5 < x < 15}")