def count_down(n):
    """Print numbers from n to 1 recursively."""
    if n == 0:
        return
    else:
        print(n)
        count_down(n - 1)

# Test the function
print("Counting down from 5:")
count_down(5)  # Should print: 5 4 3 2 1

countdown = int(input("Enter countdown start: "))
count_down(countdown)