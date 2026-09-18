class Student:
    def __init__(self, name):
        self.name = name


class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)


student1 = Student("Rane")
course1 = Course("Comsci")

course1.add_student(student1)

print(course1.students[0].name)
