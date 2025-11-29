# Create a class Circle containing an instance variable radius. The class also contains two
# instance methods area() and circumference() to find area and circumference of circles
# respectively. Use this class to find area and circumference of two different circles. Use PI as a
# class variable.

import math

class Circle:
    PI = math.pi  # Class variable for PI

    def __init__(self, radius):
        self.radius = radius  # Instance variable for radius

    def area(self):
        return Circle.PI * (self.radius ** 2)  # Area = PI * r^2

    def circumference(self):
        return 2 * Circle.PI * self.radius  # Circumference = 2 * PI * r

# Input for first circle
radius1 = float(input("Enter radius of Circle 1: "))
circle1 = Circle(radius1)

# Input for second circle
radius2 = float(input("Enter radius of Circle 2: "))
circle2 = Circle(radius2)

# Calculate and display area and circumference for Circle 1
print(f"Circle 1 - Area: {circle1.area()}, Circumference: {circle1.circumference()}")

# Calculate and display area and circumference for Circle 2
print(f"Circle 2 - Area: {circle2.area()}, Circumference: {circle2.circumference()}")
