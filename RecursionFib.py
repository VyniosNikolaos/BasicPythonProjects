def fibonacci(n):
    # Base cases: if n is 0 or 1, return n
    if n <= 1:
        return n
    # Recursive case: sum of the two preceding numbers
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Test the function
for i in range(10):
    print(f"Fibonacci({i}) = {fibonacci(i)}")