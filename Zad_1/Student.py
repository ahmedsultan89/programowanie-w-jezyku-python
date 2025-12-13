class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        average = sum(self.marks) / len(self.marks)
        return average > 50


# Example students
student_pass = Student("Ahmed", [70, 80, 90])
student_fail = Student("John", [30, 40, 45])

# Test results
print(student_pass.is_passed())
print(student_fail.is_passed())