# Write a program to count number of alphabets, digits, and whitespaces in a string.

def count_characters(input_string):
    alphabets = 0
    digits = 0
    whitespaces = 0

    for char in input_string:
        if char.isalpha():
            alphabets += 1
        elif char.isdigit():
            digits += 1
        elif char.isspace():
            whitespaces += 1

    return alphabets, digits, whitespaces

input_string = input("Enter a string: ")
alphabets, digits, whitespaces = count_characters(input_string)
print("Number of alphabets:", alphabets)
print("Number of digits:", digits)
print("Number of whitespaces:", whitespaces)
