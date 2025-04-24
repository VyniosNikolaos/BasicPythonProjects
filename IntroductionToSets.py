# Creating a set
fruits = {"apple", "banana", "cherry"}
print(f"Fruit set: {fruits}")

# Creating a set from a list (removes duplicates)
numbers = set([1, 2, 2, 3, 4, 4, 5])
print(f"Number set: {numbers}")

# Adding elements to a set
fruits.add("date")
print(f"Fruits after adding 'date': {fruits}")

# Removing elements from a set
fruits.remove("banana")
print(f"Fruits after removing 'banana': {fruits}")

# Removing an element safely (no error if not found)
fruits.discard("kiwi")
print(f"Fruits after discarding 'kiwi': {fruits}")

# Checking if an item is in the set
has_apple = "apple" in fruits
print(f"Is 'apple' in the set? {has_apple}")

# Set length
set_length = len(fruits)
print(f"Number of fruits: {set_length}")

# Sets are unordered
print("Sets are unordered. This might print in a different order:")
for fruit in fruits:
    print(fruit)

# Sets only contain unique elements
unique_letters = set("hello")
print(f"Unique letters in 'hello': {unique_letters}")

# Creating an immutable (frozen) set
frozen_set = frozenset([1, 2, 3])
print(f"Frozen set: {frozen_set}")