# Admission to a professional course is subject to the following conditions:
# a) Marks in mathematics >=60
# b) Marks in physics >=50
# c) Marks in chemistry >=40
# d) Total in all three subjects >=200

# Or

# Total in mathematics and physics>=150
# Given the marks in three subjects, write a program to process the applications to list eligible
# candidates.

def is_eligible(maths, physics, chemistry):
    total = maths + physics + chemistry

    if (maths >= 60 and physics >= 50 and chemistry >= 40 and total >= 200) or (maths + physics >= 150):
        return True
    return False

def main():
    maths = float(input("Enter marks in Mathematics: "))
    physics = float(input("Enter marks in Physics: "))
    chemistry = float(input("Enter marks in Chemistry: "))

    if is_eligible(maths, physics, chemistry):
        print("You are eligible for admission.")
    else:
        print("You are not eligible for admission.")

# Run the program if the script is executed directly from the command line
# This allows the script to be imported without executing the main function
# when used as a module in another script.
if __name__ == "__main__":
    main()
