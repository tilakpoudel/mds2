# The rates of tax on gross salary are as shown below:
# Income Tax
# Less than 10,000 Nill
# Rs. 10,000 to 19,999 10%
# Rs. 20,000 to 39,999 15%
# Rs. 40,000 to above 20%
# Write a program to compute the net salary after deducting the tax for the given information
# and print the same.

gross_salary = float(input("Enter gross salary: "))
if gross_salary < 10000:
    tax = 0
elif gross_salary < 20000:
    tax = gross_salary * 0.10
elif gross_salary < 40000:
    tax = gross_salary * 0.15
else:
    tax = gross_salary * 0.20
net_salary = gross_salary - tax
print("Net salary: ", net_salary)
# Output the net salary after tax deduction
print(f"Net salary after tax deduction is: {net_salary}")
# Output the tax amount
print(f"Tax amount deducted is: {tax}")
# Output the gross salary
print(f"Gross salary was: {gross_salary}")
