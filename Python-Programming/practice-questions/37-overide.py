# Overload + operator in Q.N.32 to add two distance objects.

class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __add__(self, other):
        total_inches = self.to_inches() + other.to_inches()
        return Distance.from_inches(total_inches)

    def to_inches(self):
        return self.feet * 12 + self.inches

    @classmethod
    def from_inches(cls, total_inches):
        feet = total_inches // 12
        inches = total_inches % 12

        return cls(feet, inches)
    
# Input for first distance object
feet1 = int(input("Enter feet for Distance 1: "))
inches1 = int(input("Enter inches for Distance 1: "))

dist1 = Distance(feet1, inches1)

# Input for second distance object
feet2 = int(input("Enter feet for Distance 2: "))
inches2 = int(input("Enter inches for Distance 2: "))

dist2 = Distance(feet2, inches2)

# Add the two distance objects using overloaded + operator
dist_sum = dist1 + dist2
# Display the result
print(f"Sum of Distance 1 and Distance 2: {dist_sum.feet} feet {dist_sum.inches} inches")
