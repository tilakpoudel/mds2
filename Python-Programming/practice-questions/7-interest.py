# Write a program to calculate the simple interest on the basis of following assumption:
# a) If balance is greater than or equal to 100000, interest is 7 %
# b) If balance is greater than or equal to 50000 and less than 100000 interest is 5 %
# c) If balance is less than 50000, interest is 3%

balance = float(input("Enter the balance amount: "))
interest = 0
# Calculate interest based on the balance amount
if balance >= 100000:
    interest = balance * 0.07
elif balance >= 50000:
    interest = balance * 0.05
else:
    interest = balance * 0.03
print("Interest: ", interest)
