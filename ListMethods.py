fruits = ["apple", "banana", "cherry"]

# Adding elements
fruits.append("date")
print(f"After append: {fruits}")

fruits.insert(1, "blueberry")
print(f"After insert: {fruits}")

fruits.extend(["elderberry", "fig"])
print(f"After extend: {fruits}")

# Removing elements
removed_fruit = fruits.pop()
print(f"Popped fruit: {removed_fruit}")
print(f"After pop: {fruits}")

fruits.remove("banana")
print(f"After remove: {fruits}")

del fruits[0]
print(f"After del: {fruits}")

# Ordering
fruits.sort()
print(f"After sort: {fruits}")

fruits.reverse()
print(f"After reverse: {fruits}")

# Counting and index
count_cherry = fruits.count("cherry")
print(f"Count of 'cherry': {count_cherry}")

index_cherry = fruits.index("cherry")
print(f"Index of 'cherry': {index_cherry}")

# Copying lists
fruits_copy = fruits.copy()
print(f"Copied list: {fruits_copy}")

# Clearing the list
fruits.clear()
print(f"After clear: {fruits}")