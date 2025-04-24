# Basic for loop with a list
fruits = ["apple", "banana", "cherry"]
print("Looping through a list:")
for fruit in fruits:
    print(fruit)

# For loop with range
print("\nLooping with range:")
for i in range(5):
    print(i)

# For loop with start, stop, and step in range
print("\nLooping with range (start, stop, step):")
for i in range(2, 10, 2):
    print(i)

# For loop with enumeration
print("\nEnumerating a list:")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# For loop with dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}
print("\nLooping through dictionary keys:")
for key in person:
    print(key)

print("\nLooping through dictionary items:")
for key, value in person.items():
    print(f"{key}: {value}")

# Nested for loops
print("\nNested for loops:")
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})", end=" ")
    print()  # New line after inner loop

# For loop with zip
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
print("\nUsing zip in for loop:")
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# For loop with a string
print("\nLooping through a string:")
for char in "Python":
    print(char)