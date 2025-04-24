# A string is a sequence of characters
simple_string = "Hello, World!"
print(f"Simple string: {simple_string}")

# Strings can be defined with single or double quotes
single_quotes = 'I am a string'
double_quotes = "I am also a string"
print(f"Single quotes: {single_quotes}")
print(f"Double quotes: {double_quotes}")

# Triple quotes for multi-line strings
multi_line = """This is a
multi-line
string."""
print(f"Multi-line string:\n{multi_line}")

# Strings are immutable (cannot be changed after creation)
name = "Alice"
# This creates a new string, it doesn't modify the original
new_name = name + " Smith"
print(f"Original name: {name}")
print(f"New name: {new_name}")

# Accessing characters in a string (indexing)
first_char = simple_string[0]
print(f"First character: {first_char}")

# Slicing strings
slice_of_string = simple_string[7:12]
print(f"Slice of string: {slice_of_string}")

# String length
length = len(simple_string)
print(f"Length of '{simple_string}': {length}")

# Strings are iterable
print("Characters in 'Hello':")
for char in "Hello":
    print(char)

# Checking if a substring exists in a string
contains_world = "World" in simple_string
print(f"Does '{simple_string}' contain 'World'? {contains_world}")