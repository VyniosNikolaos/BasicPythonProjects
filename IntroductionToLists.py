# Creating a list
fruits = ["apple", "banana", "cherry"]
print(f"Fruit list: {fruits}")

# Lists can contain different types
mixed_list = [1, "hello", 3.14, True]
print(f"Mixed list: {mixed_list}")

# Accessing elements (indexing)
first_fruit = fruits[0]
print(f"First fruit: {first_fruit}")

# Negative indexing (from the end)
last_fruit = fruits[-1]
print(f"Last fruit: {last_fruit}")

# Slicing lists
slice_of_fruits = fruits[1:3]
print(f"Slice of fruits: {slice_of_fruits}")

# Lists are mutable (can be changed)
fruits[1] = "blueberry"
print(f"Updated fruit list: {fruits}")

# Length of a list
list_length = len(fruits)
print(f"Number of fruits: {list_length}")

# Checking if an item is in the list
has_apple = "apple" in fruits
print(f"Is 'apple' in the list? {has_apple}")

# Lists can be nested
nested_list = [1, [2, 3, 4], 5]
print(f"Nested list: {nested_list}")
print(f"Second element of nested list: {nested_list[1]}")
print(f"First element of nested list's second element: {nested_list[1][0]}")