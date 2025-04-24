# Creating a dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(f"Person dictionary: {person}")

# Accessing values
name = person["name"]
print(f"Name: {name}")

# Using get() method (safer if key might not exist)
age = person.get("age", "Unknown")
print(f"Age: {age}")

# Modifying values
person["age"] = 31
print(f"Updated person: {person}")

# Adding new key-value pairs
person["occupation"] = "Engineer"
print(f"Person with occupation: {person}")

# Removing key-value pairs
del person["city"]
print(f"Person after removing city: {person}")

# Checking if a key exists
has_name = "name" in person
print(f"Does person have 'name'? {has_name}")

# Dictionary length
dict_length = len(person)
print(f"Number of key-value pairs: {dict_length}")

# Nested dictionaries
nested_dict = {
    "person1": {"name": "Alice", "age": 30},
    "person2": {"name": "Bob", "age": 25}
}
print(f"Nested dictionary: {nested_dict}")
print(f"Person2's age: {nested_dict['person2']['age']}")