def power(base, exponent):
    """Calculate base raised to the power of exponent recursively."""
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)

# Test the function
print("2 to the power of 4:", power(2, 4))  # Should print: 2 to the power of 4: 16
print("3 to the power of 3:", power(3, 3))  # Should print: 3 to the power of 3: 27