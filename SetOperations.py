set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union of sets
union_set = set1.union(set2)
print(f"Union of set1 and set2: {union_set}")

# Intersection of sets
intersection_set = set1.intersection(set2)
print(f"Intersection of set1 and set2: {intersection_set}")

# Difference of sets
difference_set = set1.difference(set2)
print(f"Difference of set1 and set2: {difference_set}")

# Symmetric difference of sets
symmetric_difference = set1.symmetric_difference(set2)
print(f"Symmetric difference of set1 and set2: {symmetric_difference}")

# Subset check
subset = {1, 2, 3}
is_subset = subset.issubset(set1)
print(f"Is {subset} a subset of set1? {is_subset}")

# Superset check
is_superset = set1.issuperset(subset)
print(f"Is set1 a superset of {subset}? {is_superset}")

# Disjoint check
set3 = {10, 11, 12}
is_disjoint = set1.isdisjoint(set3)
print(f"Are set1 and set3 disjoint? {is_disjoint}")

# Modifying sets
set1.update(set2)
print(f"set1 after update with set2: {set1}")

set1.intersection_update(set2)
print(f"set1 after intersection_update with set2: {set1}")

set1.difference_update(set2)
print(f"set1 after difference_update with set2: {set1}")

# Removing elements
popped_element = set2.pop()
print(f"Popped element from set2: {popped_element}")
print(f"set2 after pop: {set2}")

# Clearing a set
set2.clear()
print(f"set2 after clear: {set2}")