def sum_digits(number):
    """Calculate the sum of digits in a number recursively."""
    if number < 10:
        return number
    else:
        return number % 10 + sum_digits(number // 10)

# Test the function
print("Sum of digits in 12345:", sum_digits(12345))  # Should print: Sum of digits in 12345: 15
print("Sum of digits in 9876:", sum_digits(9876))  # Should print: Sum of digits in 9876: 30