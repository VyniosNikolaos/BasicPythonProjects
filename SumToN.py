def sum_to_n(n):
    """Calculate the sum of numbers from 1 to n recursively."""
    if n == 1:
        return 1
    else:
        return n + sum_to_n(n - 1)

# Test the function
print("Sum to 5:", sum_to_n(5))  # Should print: Sum to 5: 15
print("Sum to 10:", sum_to_n(10))  # Should print: Sum to 10: 55