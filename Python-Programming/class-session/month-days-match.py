# Print number of days in a month using match-case statement.
# This program takes the month number as input and prints the number of days in that month using match-case statement.
month = int(input("Enter month number (1-12): "))

match month:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print("31 days")
    case 4 | 6 | 9 | 11:
        print("30 days")
    case 2:
        print("28 or 29 days (February)")
    case _:
        print("Invalid month number. Please enter a number between 1 and 12.")
