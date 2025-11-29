# Write a program to check whether a number is palindrome or not.
# A palindrome number reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.
def is_palindrome(number):
    original_number = str(number)
    reversed_number = original_number[::-1]
    return original_number == reversed_number

number = input("Enter a number: ")
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
