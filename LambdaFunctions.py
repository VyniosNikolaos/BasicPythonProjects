# Basic lambda function
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

# Lambda with multiple arguments
add = lambda x, y: x + y
print(f"5 + 3 = {add(5, 3)}")

# Lambda with conditional expression
is_even = lambda x: True if x % 2 == 0 else False
print(f"Is 4 even? {is_even(4)}")
print(f"Is 5 even? {is_even(5)}")

# Using lambda in sort function
pairs = [(1, 'one'), (3, 'three'), (2, 'two'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(f"Sorted pairs: {pairs}")

# Lambda with dictionary operations
people = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, {'name': 'Charlie', 'age': 35}]
sorted_people = sorted(people, key=lambda person: person['age'])
print(f"People sorted by age: {sorted_people}")

# Lambda in higher-order functions
def multiply_by(n):
    return lambda x: x * n

double = multiply_by(2)
triple = multiply_by(3)

print(f"Double of 5: {double(5)}")
print(f"Triple of 5: {triple(5)}")

# Immediately Invoked Lambda Expression (IILE)
result = (lambda x: x ** 2 + 5*x + 4)(3)
print(f"Result of quadratic expression for x=3: {result}")

# Lambda with default arguments
greet = lambda name, greeting="Hello": f"{greeting}, {name}!"
print(greet("Alice"))
print(greet("Bob", "Hi"))