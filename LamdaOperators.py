# Python: Lambda with map(), filter(), and reduce()

from functools import reduce

# Sample data
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
people = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, {'name': 'Charlie', 'age': 35}]

# Using lambda with map()
squared = list(map(lambda x: x**2, numbers))
print(f"Squared numbers: {squared}")

names = list(map(lambda person: person['name'], people))
print(f"Names: {names}")

# Using lambda with filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")

adults = list(filter(lambda person: person['age'] >= 30, people))
print(f"Adults: {adults}")

# Using lambda with reduce()
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(f"Sum of numbers: {sum_of_numbers}")

product_of_numbers = reduce(lambda x, y: x * y, numbers)
print(f"Product of numbers: {product_of_numbers}")

# Combining map() and filter()
odd_squares = list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, numbers)))
print(f"Squares of odd numbers: {odd_squares}")

# Using lambda with max() and min()
oldest_person = max(people, key=lambda person: person['age'])
print(f"Oldest person: {oldest_person}")

youngest_person = min(people, key=lambda person: person['age'])
print(f"Youngest person: {youngest_person}")

# Advanced example: Grouping with lambda and reduce
from collections import defaultdict

grouped = reduce(lambda acc, person: acc[person['age']].append(person['name']) or acc, 
                 people, 
                 defaultdict(list))
print(f"Grouped by age: {dict(grouped)}")

# Chaining map() and reduce()
sum_of_squares = reduce(lambda x, y: x + y, map(lambda x: x**2, numbers))
print(f"Sum of squares: {sum_of_squares}")