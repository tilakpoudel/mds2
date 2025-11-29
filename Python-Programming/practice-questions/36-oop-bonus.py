# Create a parent class Bonus with instance variables sales_id and sales_amount. Add get_bonus
# method that calculates a salesperson’s bonus using the foumula bonus = sales * 0.05. Create a
# child class named PremiumBonus from Bonus. The child class’s get_premium_bonus()
# method should calculate the bonus using the formula bonus = sales * 0.05 + (sales – 2500) *
# 0.01. Now, create an object of PremiumBonus class and use this object to find both bonus and
# premium bonus.

class Bonus:
    def __init__(self, sales_id, sales_amount):
        self.sales_id = sales_id
        self.sales_amount = sales_amount

    def get_bonus(self):
        return self.sales_amount * 0.05
    
class PremiumBonus(Bonus):
    def get_premium_bonus(self):
        base_bonus = self.get_bonus()
        additional_bonus = 0

        if self.sales_amount > 2500:
            additional_bonus = (self.sales_amount - 2500) * 0.01

        return base_bonus + additional_bonus
    
# Input for sales_id and sales_amount
sales_id = input("Enter Sales ID: ")
sales_amount = float(input("Enter Sales Amount: "))

premium_bonus_obj = PremiumBonus(sales_id, sales_amount)

# Calculate and display bonus and premium bonus
print(f"Bonus: {premium_bonus_obj.get_bonus()}")
print(f"Premium Bonus: {premium_bonus_obj.get_premium_bonus()}")
