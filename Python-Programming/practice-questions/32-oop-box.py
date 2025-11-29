# Create a class Box with instance variables width, height and depth. The class also contains
# instance methods volume() and surface_area() to find volume and surface area of boxes
# respectively. Use this class to find volume and surface area of two different boxes.

class Box:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def volume(self):
        return self.width * self.height * self.depth

    def surface_area(self):
        return 2 * (self.width * self.height + self.height * self.depth + self.depth * self.width)
    
# Input for first box
width1 = float(input("Enter width of Box 1: "))
height1 = float(input("Enter height of Box 1: "))
depth1 = float(input("Enter depth of Box 1: "))

box1 = Box(width1, height1, depth1)

# Input for second box
width2 = float(input("Enter width of Box 2: "))
height2 = float(input("Enter height of Box 2: "))
depth2 = float(input("Enter depth of Box 2: "))

box2 = Box(width2, height2, depth2)

# Calculate and display volume and surface area for Box 1
print(f"Box 1 - Volume: {box1.volume()}, Surface Area: {box1.surface_area()}")

# Calculate and display volume and surface area for Box 2
print(f"Box 2 - Volume: {box2.volume()}, Surface Area: {box2.surface_area()}")
