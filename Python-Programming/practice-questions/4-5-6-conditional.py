# Write a program to calculate discount on the basis of following assumption:
# a) If purchased amount is greater than or equal to 5000, discount is 10%
# b) If purchased amount is greater than or equal to 4000 and less than 5000, discount is 7%
# c) If purchased amount is greater than or equal to 3000 and less than 4000, discount is 5%
# d) If purchased amount is greater than or equal to 2000 and less than 3000, discount is 3%
# e) If purchased amount is less than 2000, discount is 2%

purchased_amount = float(input("Enter purchased amount: "))
discount = 0

# Calculate discount based on the purchased amount
if purchased_amount >= 5000:
    discount = purchased_amount * 0.10
elif purchased_amount >= 4000:
    discount = purchased_amount * 0.07
elif purchased_amount >= 3000:
    discount = purchased_amount * 0.05
elif purchased_amount >= 2000:
    discount = purchased_amount * 0.03
else:
    discount = purchased_amount * 0.02
print("Discount: ", discount)
