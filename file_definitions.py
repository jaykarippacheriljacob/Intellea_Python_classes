# 1. open() - Opens a file and returns a file object; syntax: open(path, mode)
file = open("students.txt", "r")

# 2. Modes:
# "r"  - Read (default); raises FileNotFoundError if the file doesn't exist.
# "w"  - Write; creates the file, or ERASES all existing content first.
# "a"  - Append; creates the file, or adds to the end without erasing.
# "x"  - Create; makes a new file, raises FileExistsError if it already exists.
# "r+" - Read and write; the file must already exist.

# 3. read() - Returns the entire file content as one string.
content = file.read()

# 4. read(n) - Returns only the next n characters.
part = file.read(5)

# 5. readline() - Returns the next single line, including its "\n" at the end.
line = file.readline()

# 6. readlines() - Returns all lines as a list of strings, each ending with "\n".
lines = file.readlines()     # ['Jay\n', 'Data Engineering\n', '90']

# 7. Looping over the file - Reads one line at a time; memory-efficient for large files.
for line in file:
    print(line.strip())      # strip() removes the trailing "\n"

# 8. write() - Writes a string to the file; doesn't add "\n" automatically.
file.write("Jay\n")

# 9. writelines() - Writes a list of strings; also doesn't add "\n" between them.
file.writelines(["Jay\n", "Chennai\n"])

# 10. close() - Closes the file and saves pending writes; always close after opening.
file.close()

# 11. with statement - Opens a file and closes it automatically, even if an error occurs.
with open("students.txt", "r") as file:
    content = file.read()

# 12. Path relative to the script - Finds files in the script's folder, wherever it's run from.
import os
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "students.txt")

# 13. os.path.exists() - Returns True if the file exists; useful before reading.
if os.path.exists(file_path):
    print("File found")

# 14. seek(0) - Moves the file pointer back to the start, so the file can be read again.
file.seek(0)

#####
# CSV Files (Comma-Separated Values)

# 1. CSV - A plain-text file that stores table data, one row per line, with values separated by commas.
#    Example file content:
#    name,course,marks
#    ravi,python,84

# 2. import csv - Built-in module for reading and writing CSV files (no installation needed).
import csv

# 3. csv.reader() - Reads a CSV file and returns each row as a list of strings.
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)            # ['ravi', 'python', '84']

# 4. next(reader) - Reads one row; commonly used to skip the header row.
    header = next(reader)     # ['name', 'course', 'marks']

# 5. csv.writer() - Creates a writer object for writing rows to a CSV file.
# 6. writerow() - Writes a single list as one row.
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "course", "marks"])
    writer.writerow(["ravi", "python", 84])

# 7. writerows() - Writes a list of lists, each as a separate row.
    writer.writerows([["arun", "sql", 74], ["meena", "excel", 90]])

# 8. csv.DictReader() - Reads each row as a dictionary, using the header row as keys.
with open("students.csv", "r") as file:
    for row in csv.DictReader(file):
        print(row["name"], row["marks"])    # ravi 84

# 9. csv.DictWriter() - Writes dictionaries as rows; fieldnames sets the column order.
with open("students.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "course", "marks"])
    writer.writeheader()                    # Writes the header row
    writer.writerow({"name": "ravi", "course": "python", "marks": 84})


#####
# JSON Files (JavaScript Object Notation)

# 10. JSON - A text format for storing structured data as key-value pairs and lists, similar to Python dictionaries.
#     Example file content:
#     {"name": "ravi", "course": "python", "marks": 85}

# 11. import json - Built-in module for converting between JSON and Python objects.
import json

# 12. json.load() - Reads a JSON file and converts it into a Python object (usually a dict or list).
with open("students.json", "r") as file:
    student = json.load(file)
    print(student["name"])                  # ravi

# 13. json.dump() - Writes a Python object to a JSON file; indent formats it for readability.
with open("students.json", "w") as file:
    json.dump({"name": "ravi", "marks": 85}, file, indent=4)

# 14. json.loads() - Converts a JSON string (not a file) into a Python object.
data = json.loads('{"name": "ravi", "marks": 85}')
print(data["marks"])                        # 85

# 15. json.dumps() - Converts a Python object into a JSON string (not a file).
text = json.dumps({"name": "ravi"})
print(text)                                 # {"name": "ravi"}
