## Multiplication table using a for Loop.

# User Input
number = int(input("Enter a number to see it's multiplication table: "))
for y in range (1, 11):
    z = number * y
    print(f"{number} * {y} = {z}")


