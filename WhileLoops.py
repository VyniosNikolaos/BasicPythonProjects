# Basic while loop
print("Basic while loop:")
count = 0
while count < 5:
    print(count)
    count += 1

# While loop with user input
print("\nWhile loop with user input:")
user_input = ""
while user_input.lower() != "quit":
    user_input = input("Enter a command (type 'quit' to exit): ")
    print(f"You entered: {user_input}")

# While loop with a boolean flag
print("\nWhile loop with a boolean flag:")
is_running = True
counter = 0
while is_running:
    print(counter)
    counter += 1
    if counter >= 5:
        is_running = False

# While loop with break
print("\nWhile loop with break:")
while True:
    print(counter)
    counter += 1
    if counter >= 10:
        break

# While loop with continue
print("\nWhile loop with continue:")
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

# While loop with else clause
print("\nWhile loop with else clause:")
n = 0
while n < 5:
    print(n)
    n += 1
else:
    print("Loop completed normally")

# Infinite loop (be careful!)
print("\nInfinite loop (stopped after 5 iterations):")
i = 0
while True:
    print(i)
    i += 1
    if i >= 5:
        print("Stopping infinite loop")
        break

# While loop for input validation
print("\nWhile loop for input validation:")
while True:
    try:
        age = int(input("Enter your age: "))
        if 0 <= age <= 120:
            print(f"Your age is {age}")
            break
        else:
            print("Please enter a valid age between 0 and 120")
    except ValueError:
        print("Please enter a valid integer for age")