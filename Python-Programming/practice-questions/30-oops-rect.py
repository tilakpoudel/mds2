# Create a class Rectangle containing instance variables length and breadth. The class also
# contains two instance methods area() and perimeter() to find area and perimeter of rectangles
# respectively. Use this class to find area and perimeter of two different rectangles.

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)
    
# Input for first rectangle
length1 = float(input("Enter length of Rectangle 1: "))
breadth1 = float(input("Enter breadth of Rectangle 1: "))

rect1 = Rectangle(length1, breadth1)

# Input for second rectangle
length2 = float(input("Enter length of Rectangle 2: "))
breadth2 = float(input("Enter breadth of Rectangle 2: "))

rect2 = Rectangle(length2, breadth2)

# Calculate and display area and perimeter for Rectangle 1
print(f"Rectangle 1 - Area: {rect1.area()}, Perimeter: {rect1.perimeter()}")

# Calculate and display area and perimeter for Rectangle 2
print(f"Rectangle 2 - Area: {rect2.area()}, Perimeter: {rect2.perimeter()}")
