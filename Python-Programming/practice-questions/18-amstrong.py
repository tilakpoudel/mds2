# 18. Write a program to check if a number is Armstrong Number or not.
# An Armstrong number of three digits is an integer such that the sum of the cubes of its digits is equal to the number itself.
# For example, 153 is an Armstrong number since 1^3 + 5^3 + 3^3 = 153.

def is_armstrong(number):
    num_str = str(number)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)

    return sum_of_powers == number

number = int(input("Enter a number: "))
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
