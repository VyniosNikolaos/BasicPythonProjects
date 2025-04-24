# Basic list comprehension
squares = [x**2 for x in range(10)]
print(f"Squares: {squares}")

# List comprehension with condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# Nested list comprehension
matrix = [[i+j for j in range(3)] for i in range(3)]
print(f"Matrix: {matrix}")

# List comprehension with strings
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(f"Uppercase words: {upper_words}")

# Flattening a 2D list
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for sublist in nested_list for num in sublist]
print(f"Flattened list: {flattened}")

# Creating a list of tuples
coordinates = [(x, y) for x in range(3) for y in range(3)]
print(f"Coordinates: {coordinates}")

# Conditional list comprehension with else
numbers = [-4, -2, 0, 2, 4]
abs_or_neg = [x if x >= 0 else -x for x in numbers]
print(f"Absolute values: {abs_or_neg}")