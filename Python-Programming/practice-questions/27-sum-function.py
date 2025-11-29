# Write a program using function with return type to find sum of two numbers.

def sum_of_two_numbers(a, b):
    return a + b

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

result = sum_of_two_numbers(num1, num2)

print(f"Sum of the two numbers: {result}")
