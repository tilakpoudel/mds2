# 12. Write a program using match-case statement to develop a simple calculator.
# I want to perform addition, subtraction, multiplication, and division operations and exit the program when the user wants to.

def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        print("Exiting the program.")
        return

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    match choice:
        case '1':
            result = num1 + num2
            operation = "Addition"
        case '2':
            result = num1 - num2
            operation = "Subtraction"
        case '3':
            result = num1 * num2
            operation = "Multiplication"
        case '4':
            if num2 != 0:
                result = num1 / num2
                operation = "Division"
            else:
                print("Error! Division by zero.")

                return
        case _:
            print("Invalid input")

            return

    print(f"{operation} of {num1} and {num2} is: {result}")

calculator()
