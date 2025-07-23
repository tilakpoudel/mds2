# Give discount of 5% if the purchase is greater than 1000.

pa = float(input("Enter purchased amount: "))
d = 0
if pa >= 1000:
    d = pa * 0.05
elif pa >= 500:
    d = pa * 0.03
else:
    d = pa * 0.02
print("Discount: ", d)
