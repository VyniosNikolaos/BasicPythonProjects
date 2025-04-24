name = "Alice"
age = 30

# 1. f-strings (Python 3.6+)
print(f"1. My name is {name} and I am {age} years old.")

# 2. .format() method
print("2. My name is {} and I am {} years old.".format(name, age))

# 3. % operator (old style, less commonly used now)
print("3. My name is %s and I am %d years old." % (name, age))

# 4. Template strings
from string import Template
t = Template('My name is $name and I am $age years old.')
print("4. " + t.substitute(name=name, age=age))

# Formatting with f-strings
pi = 3.14159
print(f"Pi to 2 decimal places: {pi:.2f}")

# Padding and alignment
for i in range(1, 4):
    print(f"Number {i:2d}, Square {i**2:3d}, Cube {i**3:4d}")

# Date formatting
import datetime
today = datetime.datetime.now()
print(f"Today's date: {today:%B %d, %Y}")

# Formatting with .format()
print("Binary: {0:b}, Octal: {0:o}, Hexadecimal: {0:x}".format(42))

# Named placeholders
print("I have a {pet} that is {age:d} years old.".format(pet="dog", age=5))

# Nested formatting
nested = {"a": {"b": "nested value"}}
print("Nested: {a[b]}".format(**nested))

# Formatting numbers
big_number = 1234567890
print(f"Formatted large number: {big_number:,}")

# Percentage formatting
percentage = 0.8525
print(f"Percentage: {percentage:.2%}")

# Aligning strings
print(f"{'Left':<10}|{'Center':^10}|{'Right':>10}")
print(f"{'a':<10}|{'b':^10}|{'c':>10}")