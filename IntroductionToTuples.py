# Creating a tuple
coordinates = (3, 4)
print(f"Coordinates: {coordinates}")

# Tuples can contain different types
mixed_tuple = (1, "hello", 3.14, True)
print(f"Mixed tuple: {mixed_tuple}")

# Creating a tuple with a single element
single_element_tuple = (42,)  # Note the comma
print(f"Single element tuple: {single_element_tuple}")

# Accessing elements (indexing)
x_coordinate = coordinates[0]
print(f"X coordinate: {x_coordinate}")

# Negative indexing (from the end)
last_element = mixed_tuple[-1]
print(f"Last element: {last_element}")

# Slicing tuples
slice_of_tuple = mixed_tuple[1:3]
print(f"Slice of tuple: {slice_of_tuple}")

# Tuples are immutable (cannot be changed)
try:
    coordinates[0] = 5
except TypeError as e:
    print(f"Error when trying to modify tuple: {e}")

# Length of a tuple
tuple_length = len(mixed_tuple)
print(f"Length of mixed tuple: {tuple_length}")

# Checking if an item is in the tuple
has_hello = "hello" in mixed_tuple
print(f"Is 'hello' in the tuple? {has_hello}")

# Tuples can be nested
nested_tuple = (1, (2, 3, 4), 5)
print(f"Nested tuple: {nested_tuple}")
print(f"Second element of nested tuple: {nested_tuple[1]}")
print(f"First element of nested tuple's second element: {nested_tuple[1][0]}")

# Unpacking tuples
a, b = coordinates
print(f"Unpacked coordinates: a = {a}, b = {b}")

# Using * to unpack remaining elements
first, *rest = mixed_tuple
print(f"First element: {first}, Rest: {rest}")