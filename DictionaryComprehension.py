# Basic dictionary comprehension
squares = {x: x**2 for x in range(5)}
print(f"Squares: {squares}")

# Dictionary comprehension with condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# Creating a dictionary from two lists
keys = ['a', 'b', 'c']
values = [1, 2, 3]
combined = {k: v for k, v in zip(keys, values)}
print(f"Combined dictionary: {combined}")

# Swapping keys and values
original = {'a': 1, 'b': 2, 'c': 3}
swapped = {v: k for k, v in original.items()}
print(f"Swapped dictionary: {swapped}")

# Filtering a dictionary
scores = {'Alice': 95, 'Bob': 75, 'Charlie': 80, 'David': 90}
high_scores = {name: score for name, score in scores.items() if score >= 90}
print(f"High scores: {high_scores}")

# Nested dictionary comprehension
matrix = {i: {j: i*j for j in range(5)} for i in range(5)}
print(f"Matrix: {matrix}")

# Creating a dictionary of character counts
word = "hello"
char_count = {char: word.count(char) for char in word}
print(f"Character count: {char_count}")