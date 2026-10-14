#####
# Sets and Set Operations
python_student = {"Ravi", "Meena", "Arun", "Ravi"}
data_student = {"Meena", "Arun", "Zara", "Meena"}

print(f"Set of python students present: {python_student}")

# Addition of an item to a set
python_student.add("Karthik")
print(f"Revised set of python students: {python_student}")

# Removal of an item from a set
print(f"Set of data students: {data_student}")
data_student.remove("Arun")
print(f"Revised set of data students after removal of Arun: {data_student}")

# Union - in either group
all_students = python_student.union(data_student)
print(f"Students present in either course, data and python: {all_students}")

# Intersection - in both grooups
both_students = python_student.intersection(data_student)
print(f"Students attending both the course: {both_students}")

# Difference - only in one specific group
only_python = python_student.difference(data_student)
print(f"Students attending only python course. {only_python}")
