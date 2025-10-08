## Drawing a simple text-based pattern using while loops and nested for loops.

# User prompt for pattern size

size = int(input("Enter the size of the pattern: "))

# Solution for drawing the pattern.

row = 0
while row < size:
    for col in range(size):
        print("*", end="")

    print()

    row += 1

