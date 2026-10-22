#####
# Working with general files.
import os

# Folder where this script is saved
base_dir = os.path.dirname(os.path.abspath(__file__))
# Full path to students.txt in that same folder
file_path = os.path.join(base_dir, "students.txt")

# 1. Opening a file and reading the entire data present inside it
file = open(file_path, "r")
content = file.read()
print(content)
file.close()

# 2. Opening a file and reading line by line from the data present
file = open(file_path, "r")
line1 = file.readline()
print("line1: ", line1)
line2 = file.readline()
print("line2: ", line2)
file.close()

# 3. Opening a file and reading the entire file but each line as an item in the list
file = open(file_path, "r")
lines = file.readlines()
print("Readlines: ", lines)
file.close()

# 4. Opening a file and writing data into the file from start
file = open(file_path, "w")
file.write("Jay\n")
file.write("Data Engineering\n")
file.write("90")
file.close()

# 5. Opening a file and appending data to the existing file
file = open(file_path, "a")
file.write("\nChennai")
file.close()

# 6. With statement
with open(file_path, "r") as file:
    content = file.read()
print(content)

#####
# Working with CSV Files
import csv

file_path = os.path.join(base_dir, "students.csv")
# 1. Reading a csv file
with open(file_path, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# 2. Writing to a csv file
with open(file_path, "w") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "course", "marks"])
    writer.writerow(["ravi", "python", 84])
    writer.writerow(["arun", "data engineering", 74])
    writer.writerow(["meena", "data analysis", 90])

#####
# Working with JSON files (JavaScript Object Notation)

import json

file_path = os.path.join(base_dir, "students.json")
# 1. Reading a json file
with open(file_path, "r") as file:
    student = json.load(file)
    print(student)
    print(student["name"])
    print(student["marks"])

# 2. Writing a json file
student_details = {
    "name":"ravi",
    "course":"python",
    "marks":85
}
with open(file_path, "w") as file:
    json.dump(student_details, file, indent=4)
