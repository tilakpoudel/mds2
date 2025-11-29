# 33. Create a class Time with three instance variables hours, minutes, and seconds. Add instance
# methods display() to display the time in hh:mm:ss format and add() to add two time objects.
# Use this class to add and display two different time objects.

class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def display(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def add(self, other):
        total_seconds = self.to_seconds() + other.to_seconds()

        return Time.from_seconds(total_seconds)

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    @classmethod
    def from_seconds(cls, total_seconds):
        hours = total_seconds // 3600
        total_seconds %= 3600
        minutes = total_seconds // 60
        seconds = total_seconds % 60

        return cls(hours, minutes, seconds)

# Input for first time object
hours1 = int(input("Enter hours for Time 1: "))
minutes1 = int(input("Enter minutes for Time 1: "))
seconds1 = int(input("Enter seconds for Time 1: "))

time1 = Time(hours1, minutes1, seconds1)

# Input for second time object
hours2 = int(input("Enter hours for Time 2: "))
minutes2 = int(input("Enter minutes for Time 2: "))
seconds2 = int(input("Enter seconds for Time 2: "))

time2 = Time(hours2, minutes2, seconds2)

# Display both time objects
print(f"Time 1: {time1.display()}")
print(f"Time 2: {time2.display()}")

# Add the two time objects
time_sum = time1.add(time2)

# Display the result
print(f"Sum of Time 1 and Time 2: {time_sum.display()}")
