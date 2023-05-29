class Student:
    def __init__(self, name, id_num, grade_level):
        self.name = name
        self.id_num = id_num
        self.grade_level = grade_level
        
    def display(self):
        print("Name:", self.name)
        print("ID Number:", self.id_num)
        print("Grade Level:", self.grade_level)

class Class:
    def __init__(self, students):
        self.students = students
        
    def display_class_roster(self):
        for student in self.students:
            student.display()
            print()

# create some students
s1 = Student("Yuri", 8349, 12)
s2 = Student("Kelpy", 2674, 12)
s3 = Student("BigGuy", 6132, 12)

# create a class and add the students to it
my_class = Class([s1, s2, s3])

# display the class roster
my_class.display_class_roster()
