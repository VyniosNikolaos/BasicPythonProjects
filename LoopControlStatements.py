# Break statement in a for loop
print("Break in for loop:")
for i in range(10):
    if i == 5:
        break
    print(i)

# Break statement in a while loop
print("\nBreak in while loop:")
count = 0
while True:
    if count == 5:
        break
    print(count)
    count += 1

# Continue statement in a for loop
print("\nContinue in for loop:")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# Continue statement in a while loop
print("\nContinue in while loop:")
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue
    print(count)

# Pass statement (placeholder)
print("\nPass statement:")
for i in range(5):
    if i == 2:
        pass
    else:
        print(i)

# Else clause in for loop
print("\nElse clause in for loop:")
for i in range(5):
    print(i)
else:
    print("Loop completed normally")

# Else clause in for loop with break
print("\nElse clause in for loop with break:")
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("This won't be printed because of the break")

# Nested loops with break
print("\nNested loops with break:")
for i in range(3):
    for j in range(3):
        if i == j == 1:
            print("Breaking inner loop")
            break
        print(f"({i}, {j})", end=" ")
    print()  # New line after inner loop

# Loop with enumerate and conditional break
print("\nLoop with enumerate and conditional break:")
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
for index, fruit in enumerate(fruits):
    if fruit.startswith("d"):
        print(f"Found fruit starting with 'd' at index {index}")
        break
    print(fruit)

# While loop with multiple conditions
print("\nWhile loop with multiple conditions:")
a, b = 0, 10
while a < 5 and b > 5:
    print(f"a = {a}, b = {b}")
    a += 1
    b -= 1