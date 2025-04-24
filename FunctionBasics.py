# Defining a simple function
def greet():
    print("Hello, World!")

# Calling the function
greet()

# Function with a parameter
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")

# Function with multiple parameters
def add_numbers(a, b):
    print(f"The sum of {a} and {b} is {a + b}")

add_numbers(5, 3)

# Function with a docstring
def multiply(a, b):
    """
    This function multiplies two numbers and returns the result.
    
    Args:
    a (int): The first number
    b (int): The second number
    
    Returns:
    int: The product of a and b
    """
    return a * b

result = multiply(4, 7)
print(f"4 * 7 = {result}")

# Printing the docstring
print(multiply.__doc__)

# Function with local variables
def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    print(f"The average is: {average}")

calculate_average([1, 2, 3, 4, 5])

# Function calling another function
def get_square(num):
    return num ** 2

def get_square_root(num):
    return num ** 0.5

def process_number(num):
    square = get_square(num)
    square_root = get_square_root(num)
    print(f"Number: {num}, Square: {square}, Square Root: {square_root}")

process_number(16)