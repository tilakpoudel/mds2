# Write a program to find sum of two numbers using command line arguments.
import sys
# This program takes two numbers from command line arguments and prints their sum.

if len(sys.argv) != 3:
    print("Usage: python sum_of_numbers.py <num1> <num2>")
else:
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        total = num1 + num2
        print("Sum of {} and {} is: {}".format(num1, num2, total))
    except ValueError:
        print("Please provide valid numbers.")
# Usage: python sum_of_numbers.py 10 20
# Output: Sum of 10.0 and 20.0 is: 30.
