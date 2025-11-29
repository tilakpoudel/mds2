# 11. Write a program to check whether a year entered is leap or not.
# A year is a leap year if it is divisible by 4 but not divisible by 100,
# except if it is also divisible by 400.
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

year = int(input("Enter a year: "))

if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
