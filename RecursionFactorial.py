def factorial(n):
    # Base case: if n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n * factorial of (n-1)
    else:
        return n * factorial(n - 1)

# Test the function
print(factorial(5))  # Should print 120
print(factorial(0))  # Should print 1
print(factorial(7))  # Should print 5040