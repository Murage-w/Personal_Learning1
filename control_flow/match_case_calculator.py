## Match case calculator

# User Input

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("What operation do you want to perform (+,-.*,/): ")

match operation:
    case "+":
        addition = num1 + num2
        print(f"The result is: {addition}")
    case "-":
        subtraction = num1 - num2
        print(f"The result is: {subtraction}")
    case "*":
        multiplication = num1 * num2
        print(f"The result is: {multiplication}")
    case "/":
        if num2 == 0:
            print(f"Cannot divide by zero")
        else:
            division = num1 / num2
            print(f"The result is: {division}")
    case _:
     print(f"Operation cannot be executed. Please choose a valid operation")
