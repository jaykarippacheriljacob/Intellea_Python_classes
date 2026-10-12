# This program demonstrates typecasting in Python.
# Fixed values
student_age = 20

# Taking input from user
student_name = input("Enter your name: ")
student_age = input("Enter your age: ")
print(f"Student Name: {student_name}")  # Output: <class 'str'>
print(f"Student Age: {student_age}")  # Output: <class 'str'>

# Typecasting
print(f"Type of student_age after typecasting: {type(student_age)}")  # Output: <class 'int'>
student_cgpa = float(input("Enter your CGPA: "))
print(f"Type of student_cgpa after typecasting: {type(student_cgpa)}")  # Output: <class 'float'>
