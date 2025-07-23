# Write a program to find the number of days in a month.
# The program should take the month number as input from the user and display the number of days in that month.
# Note: February can have 28 or 29 days depending on whether it's a leap year or not, but for simplicity, we will consider it as 28 days in this example.

month = int(input("Enter month number (1-12): "))

if month < 1 or month > 12:
    print("Invalid month number. Please enter a number between 1 and 12.")
else:
    if month in [1, 3, 5, 7, 8, 10, 12]:
        print("31 days")
    elif month in [4, 6, 9, 11]:
        print("30 days")
    elif month == 2:
        print("28 or 29 days (February)")
    else:
        print("Invalid month number. Please enter a number between 1 and 12.")

