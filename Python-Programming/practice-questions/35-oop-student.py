# Create a class Student with instance variables name, roll_number, and marks in five subjects.
# Add three instance methods in this class to calculate total(), percentage(), and division() of the
# marks obtained by the students. Use this class to find total marks obtained, percentage, and
# division of five students.

class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks  # marks should be a list of five subject marks

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / len(self.marks)

    def division(self):
        perc = self.percentage()
        if perc >= 60:
            return "First Division"
        elif perc >= 50:
            return "Second Division"
        elif perc >= 40:
            return "Third Division"
        else:
            return "Fail"
        
students = []

for i in range(5):
    name = input(f"Enter name of Student {i + 1}: ")
    roll_number = input(f"Enter roll number of Student {i + 1}: ")
    marks = []

    for j in range(5):
        mark = float(input(f"Enter marks for subject {j + 1} of Student {i + 1}: "))
        marks.append(mark)
    
    student = Student(name, roll_number, marks)
    students.append(student)

for student in students:
    print(f"Student: {student.name}, Roll Number: {student.roll_number}")
    print(f"Total Marks: {student.total()}")
    print(f"Percentage: {student.percentage():.2f}%")
    print(f"Division: {student.division()}")
    print()
