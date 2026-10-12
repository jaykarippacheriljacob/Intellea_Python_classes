# This is a simple program to demonstrate variable assignment and printing in Python.
student_name = "Buvana"
print(f"Name of the student is: {student_name}")

# 1. do not start variable name with number
2student_name = "Buvana"  # This will cause a syntax error because variable names cannot start with a number.
print(f"Name of the student is: {2student_name}")

# 2. no spaces in variable name
student name = "Buvana"  # This will cause a syntax error because variable names cannot contain spaces.
print(f"Name of the student is: {student name}")

# 3. Case sensitivity in variable names
Student_Name = "Buvana"
student_name = "Arun"
print(f"Student_Name: {Student_Name}")  # This will print "Buvana"
print(f"student_name: {student_name}")  # This will print "Arun"