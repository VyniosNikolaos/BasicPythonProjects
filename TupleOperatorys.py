# Creating tuples
tuple1 = (1, 2, 3, 2, 4, 2)
tuple2 = ('a', 'b', 'c')

# Counting occurrences
count_2 = tuple1.count(2)
print(f"Count of 2 in tuple1: {count_2}")

# Finding index of an element
index_3 = tuple1.index(3)
print(f"Index of 3 in tuple1: {index_3}")

# Concatenating tuples
concatenated = tuple1 + tuple2
print(f"Concatenated tuple: {concatenated}")

# Repeating tuples
repeated = tuple2 * 3
print(f"Repeated tuple: {repeated}")

# Tuple comparison
tuple3 = (1, 2, 3)
tuple4 = (1, 2, 4)
print(f"tuple3 == tuple4: {tuple3 == tuple4}")
print(f"tuple3 < tuple4: {tuple3 < tuple4}")

# Using tuples as dictionary keys
coordinate_dict = {(0, 0): 'origin', (1, 0): 'right', (0, 1): 'up'}
print(f"Coordinate dictionary: {coordinate_dict}")

# Converting list to tuple
list_to_convert = [1, 2, 3]
converted_tuple = tuple(list_to_convert)
print(f"Converted list to tuple: {converted_tuple}")

# Using the sorted() function (returns a list)
sorted_tuple = tuple(sorted(tuple1))
print(f"Sorted tuple: {sorted_tuple}")

# Getting max and min values
max_value = max(tuple1)
min_value = min(tuple1)
print(f"Max value in tuple1: {max_value}")
print(f"Min value in tuple1: {min_value}")

# Using all() and any()
all_true = all(tuple1)  # Are all elements True?
any_true = any(tuple1)  # Is any element True?
print(f"All elements in tuple1 are True: {all_true}")
print(f"Any element in tuple1 is True: {any_true}")