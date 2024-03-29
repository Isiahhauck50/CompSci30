from time import sleep
from Lib_f.simple_library import get_greeting
from Lib_f.students_library import get_student_info

# Use the time module to pause the program for 2 seconds
print("Pausing for 2 seconds...")
sleep(2)

# Use the simple_lib module to get a greeting
greeting = get_greeting()
print(greeting)

# Use the time module to pause the program for 2 seconds
print("Pausing for 2 seconds...")
sleep(2)

# Use the info_lib module to get student information
students = get_student_info()
print("Student information:")
for student in students:
    print(student["name"], "-", student["major"])
