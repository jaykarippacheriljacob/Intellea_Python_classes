#####
# Dictionary: Creating, Accessing, Modifying and Looping
student = {
    "name" : "ravi",
    "age" : 21,
    "course" : "python",
    "marks" : 85
}

# Accessing the value using the key
print(f"Name: {student["name"]}")
print(f"Marks: {student["marks"]}")

# Modifying the value present
student["marks"] = 82
print(f"Revised Marks: {student["marks"]}")
 
# Looping over the dictionary items
for key, value in student.items():
    print(f"Key = {key} || Value = {value}")
