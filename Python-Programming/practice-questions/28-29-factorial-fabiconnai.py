# Write a program using recursive function to find factorial of a number.
# Write a program using recursive function to find nth Fibonacci number.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
number = int(input("Enter a number to find its factorial: "))

print(f"Factorial of {number} is {factorial(number)}")

fib_number = int(input("Enter a number to find its Fibonacci number: "))
print(f"Fibonacci number at position {fib_number} is {fibonacci(fib_number)}")
