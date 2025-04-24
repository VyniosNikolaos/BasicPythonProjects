# Positional arguments
def greet(name, greeting):
    print(f"{greeting}, {name}!")

greet("Alice", "Hello")
greet("Good morning", "Bob")  # Note the order matters for positional arguments

# Keyword arguments
greet(greeting="Hi", name="Charlie")
greet(name="David", greeting="Hey")  # Order doesn't matter for keyword arguments

# Default parameter values
def greet_with_default(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet_with_default("Eve")
greet_with_default("Frank", "Bonjour")

# Mixing positional and keyword arguments
def display_info(name, age, city):
    print(f"{name} is {age} years old and lives in {city}.")

display_info("Grace", 30, city="New York")

# Variable number of positional arguments (*args)
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3))
print(sum_all(1, 2, 3, 4, 5))

# Variable number of keyword arguments (**kwargs)
def print_key_values(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_key_values(name="Alice", age=30, city="London")

# Combining different types of arguments
def func(a, b, *args, **kwargs):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

func(1, 2, 3, 4, 5, x=10, y=20)

# Return statements
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

print(divide(10, 2))
print(divide(10, 0))

# Multiple return values
def min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = min_max([1, 2, 3, 4, 5])
print(f"Min: {minimum}, Max: {maximum}")

# Return with conditional statements
def absolute_value(num):
    if num >= 0:
        return num
    else:
        return -num

print(absolute_value(5))
print(absolute_value(-3))