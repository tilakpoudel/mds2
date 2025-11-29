# 16. Write a program to find sum of digits of a number.

def sum_of_digits(number):
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number //= 10
    return total

number = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(number))
