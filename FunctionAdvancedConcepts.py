# Function annotations (type hinting)
# This function takes a string 'name' as input and returns a greeting string.
def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet("Alice"))
# Print the annotations of the 'greet' function
print(greet.__annotations__)

# Lambda functions (anonymous functions)
# Define a lambda function to calculate the square of a number
square = lambda x: x ** 2
print(square(5))

# Using lambda with built-in functions
# Use the 'map' function to apply the lambda function to each element in the list 'numbers'
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)

# Nested functions
# Define an outer function that returns an inner function
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

# Create a new function 'add_five' by calling 'outer_function' with 5
add_five = outer_function(5)
print(add_five(3))

# Closures
# Define a function that returns another function (closure)
def multiplier(n):
    def multiply(x):
        return x * n
    return multiply

# Create two multiplier functions
times_two = multiplier(2)
times_three = multiplier(3)

print(times_two(5))
print(times_three(5))

# Decorators
# Define a decorator that converts the result of a function to uppercase
def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

# Apply the decorator to the 'say_hello' function
@uppercase_decorator
def say_hello():
    return "hello, world!"

print(say_hello())

# Recursive functions
# Define a recursive function to calculate the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

# Generators
# Define a generator function that counts down from a given number
def countdown(n):
    while n > 0:
        yield n
        n -= 1

# Use the generator function in a for loop
for number in countdown(5):
    print(number)

# Function as first-class objects
# Define a function that applies an operation to two numbers
def apply_operation(operation, x, y):
    return operation(x, y)

# Define two simple functions for addition and multiplication
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

# Use the 'apply_operation' function with 'add' and 'multiply'
print(apply_operation(add, 5, 3))
print(apply_operation(multiply, 5, 3))