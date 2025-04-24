person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Getting all keys
keys = person.keys()
print(f"Keys: {keys}")

# Getting all values
values = person.values()
print(f"Values: {values}")

# Getting all key-value pairs as tuples
items = person.items()
print(f"Items: {items}")

# Updating the dictionary
person.update({"occupation": "Engineer", "age": 31})
print(f"Updated person: {person}")

# Removing and returning an item
removed_item = person.pop("city")
print(f"Removed item: {removed_item}")
print(f"Person after removal: {person}")

# Removing and returning the last inserted item
last_item = person.popitem()
print(f"Last item removed: {last_item}")
print(f"Person after popitem: {person}")

# Clearing the dictionary
person.clear()
print(f"Cleared person: {person}")

# Creating a new dictionary with default values
fruits = dict.fromkeys(["apple", "banana", "cherry"], 0)
print(f"Fruits dictionary: {fruits}")

# Getting a value with a default if key doesn't exist
age = person.get("age", 25)
print(f"Age (with default): {age}")

# Setting a default value if key doesn't exist
person.setdefault("name", "Unknown")
print(f"Person after setdefault: {person}")