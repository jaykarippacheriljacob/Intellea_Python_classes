"""
    ASSIGNMENT SUBMITTED BY: JAY K JACOB
    Due Tue 20 Oct, 5:00 am
    Employee Skills Management System
    Set by Hemalatha · marked out of 10
    Problem Statement

    An IT company wants to maintain employee information and analyse the technical skills available across its teams. Write a Python program using dictionaries and sets to manage employee records and compare team skills.

    Requirements

    Create a dictionary containing at least three employees. Use employee IDs as keys and nested dictionaries to store each employee's name, department, and salary.

    Display all employee details using a loop and the items() method.

    Update the salary of one employee.

    Add a new employee to the dictionary.

    Retrieve an employee's department using the get() method.

    Check whether a particular employee ID exists in the dictionary using the in operator.

    Create two sets containing the technical skills available in Team A and Team B.

    Find all unique skills available across both teams using union.

    Find the skills common to both teams using intersection.

    Find the skills available only in Team A using difference.

    Find the skills available in either team but not both using symmetric difference.

    Create a list containing duplicate employee IDs and convert it into a set to identify unique employee IDs.

    Display the total number of employee ID entries and the number of unique employee IDs using len().

    Sample Data

    Employee Details:

    Employee 101: Arun, IT, Salary 35000

    Employee 102: Priya, Data Analytics, Salary 40000

    Employee 103: Kumar, Development, Salary 45000

    Team A Skills: Python, SQL, Excel, Power BI

    Team B Skills: SQL, Java, Power BI, Tableau

    Employee ID List: [101, 102, 101, 103, 102, 104]

    Expected Output Format

    --- Employee Details ---
    Employee ID: 101
    Name: Arun
    Department: IT
    Salary: 35000

    Employee ID: 102
    Name: Priya
    Department: Data Analytics
    Salary: 40000

    Employee ID: 103
    Name: Kumar
    Department: Development
    Salary: 45000

    --- Updated Employee Records ---
    Display the updated employee details

    Department Lookup: IT
    Employee ID Exists: True

    --- Team Skills Analysis ---
    All Unique Skills: ...
    Common Skills: ...
    Team A Only: ...
    Skills in Either Team but Not Both: ...

    --- Employee ID Analysis ---
    Total Employee ID Entries: 6
    Unique Employee IDs: 4
    Unique IDs: ...

    Note: Set elements may appear in any order.

    Rules

    Use dictionaries and nested dictionaries for employee records.

    Use sets for unique values and skill comparisons.

    Use loops, conditional statements, and dictionary/set methods covered in class.

    Do not use external libraries, classes, or functions.

    Write the complete program independently and test it in VS Code.
"""

# 1. Creating a dictionary of employees with nested dictionaries
employees = {}
employees[101] = {"name":"Arun", "department":"IT", "salary":35000}
employees[102] = {"name": "Priya", "department": "Data Analytics", "salary": 40000}
employees[103] = {"name": "Kumar", "department": "Development", "salary": 45000}

# 2. Displaying all employee details using a loop and the items() method.
print("--- Employee Details ---")
for emp_id, details in employees.items():
    print(f"Employee ID: {emp_id}")
    for key, value in details.items():
        print(f"{key.title()}: {value}")
    print()

# 3. Updating the salary of one employee.
employees[102].update({"salary": 48000})
# alternative
# employees[102]["salary"] = 48000

# 4. Adding a new employee to the dictionary.
employees[104] = {"name": "Meera", "department": "HR", "salary": 38000}

print("--- Updated Employee Records ---")
for emp_id, details in employees.items():
    print(f"Employee ID: {emp_id}")
    for key, value in details.items():
        print(f"{key.title()}: {value}")
    print()

# 5. Retrieving an employee's department using the get() method.
dept = employees[101].get("department")
print(f"Department Lookup: {dept}")

# 6. Checking whether a particular employee ID exists in the dictionary using the in operator.
print(f"Employee ID Exists: {103 in employees}")

# 7. Creating two sets containing the technical skills available in Team A and Team B.
skill_teamA = {"Python", "SQL", "Excel", "Power BI"}
skill_teamB = {"SQL", "Java", "Power BI", "Tableau"}

# 8. Finding all unique skills available across both teams using union.
print("--- Team Skills Analysis ---")
print(f"All Unique Skills: {skill_teamA.union(skill_teamB)}")

# 9. Finding the skills common to both teams using intersection.
print(f"Common Skills: {skill_teamA.intersection(skill_teamB)}")

# 10. Finding the skills available only in Team A using difference.
print(f"Team A Only: {skill_teamA.difference(skill_teamB)}")

# 11. Finding the skills available in either team but not both using symmetric difference.
print(f"Skills in Either Team but Not Both: {skill_teamA.symmetric_difference(skill_teamB)}")

# 12. Creating a list containing duplicate employee IDs and convert it into a set to identify unique employee IDs.
emp_id_list = [101, 102, 101, 103, 102, 104]
unique_ids = set(emp_id_list)

# 13. Displaying the total number of employee ID entries and the number of unique employee IDs using len().
print("\n--- Employee ID Analysis ---")
print(f"Total Employee ID Entries: {len(emp_id_list)}")
print(f"Unique Employee IDs: {len(unique_ids)}")
print(f"Unique IDs: {unique_ids}")
