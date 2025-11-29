# Create a class Distance containing instance variables feet and inches. The class also contains
# instance methods add() and compare() to add and compare two distance objects respectively.
# Use this class to create two different distance objects and add and compare these two distance
# objects.

class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def add(self, other):
        total_inches = self.to_inches() + other.to_inches()
        return Distance.from_inches(total_inches)

    def compare(self, other):
        return self.to_inches() - other.to_inches()

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

# Add the two distance objects
dist_sum = dist1.add(dist2)

# Compare the two distance objects
comparison = dist1.compare(dist2)
if comparison > 0:
    print("Distance 1 is greater than Distance 2")
elif comparison < 0:
    print("Distance 1 is less than Distance 2")
else:
    print("Distance 1 is equal to Distance 2")

# Display the result
print(f"Sum of Distance 1 and Distance 2: {dist_sum.feet} feet {dist_sum.inches} inches")
