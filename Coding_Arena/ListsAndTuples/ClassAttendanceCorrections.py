"""
    Class Attendance Corrections
    Medium
    Lists
    Given the list names, make three changes in order:

    Remove the first occurrence of remove_name. Print Removed: <name>, or Not found: <name> if it is not in the list.
    Insert new_name at index position.
    Pop the last name and print Popped: <name>.
    Then print the final list.

    Input Format

    Line 1: number of names n
    Next n lines: the names
    Next line: name to remove
    Next line: insert position
    Next line: name to insert
    Output Format

    Line 1: Removed: <name> or Not found: <name>
    Line 2: Popped: <name>
    Line 3: the final list
    Examples

    Input: 4 Ravi Asha Meena Ravi Ravi 1 Kiran
    Output: Removed: Ravi Popped: Ravi ['Asha', 'Kiran', 'Meena']
    Explanation: Removing the first Ravi gives [Asha, Meena, Ravi]. Inserting Kiran at 1 and popping the last name leaves [Asha, Kiran, Meena].
    Input: 3 Dev Sita Nila Arun 0 Bala
    Output: Not found: Arun Popped: Nila ['Bala', 'Dev', 'Sita']
    Explanation: Arun is not in the list. Bala goes to index 0, then Nila is popped.
    Constraints

    1 <= n <= 30
    Names have only letters and no spaces
    0 <= position <= length of the list after the removal
    Use list methods. Do not use loops except to read the names
"""

# Read the number of names
n = int(input())
# List to store the names
names = []
# Read each name and add it to the list
for i in range(n):
    names.append(input())
# Read the name to remove, the insert position and the name to insert
remove_name = input()
position = int(input())
new_name = input()

# Remove the name only if it's in the list, to avoid a ValueError
if remove_name in names:
    names.remove(remove_name)
    print(f"Removed: {remove_name}")
else:
    print(f"Not found: {remove_name}")

# Insert the new name at the given position
names.insert(position, new_name)
# Remove and return the last name in the list
last_name = names.pop(-1)
print(f"Popped: {last_name}")
# Display the final list
print(names)

# Test cases: [names, remove_name, position, new_name]
test_cases = [
    [["Arun", "Priya", "Ravi", "Meena"], "Priya", 1, "Kumar"],
    # Removed: Priya, Popped: Meena, ['Arun', 'Kumar', 'Ravi']
    [["Arun", "Ravi"], "Jay", 0, "Asha"],
    # Not found: Jay, Popped: Ravi, ['Asha', 'Arun']
    [["Arun", "Ravi", "Meena"], "Arun", 10, "Nila"],
    # Removed: Arun, Popped: Nila, ['Ravi', 'Meena']  (position past the end inserts at the end)
    [["Arun"], "Arun", 0, "Dev"],
    # Removed: Arun, Popped: Dev, []
]

# Run the same steps for each test case
for t, (lst, rem, pos, new) in enumerate(test_cases, start=1):
    print(f"\n--- Test {t} ---")
    if rem in lst:
        lst.remove(rem)
        print(f"Removed: {rem}")
    else:
        print(f"Not found: {rem}")
    lst.insert(pos, new)
    print(f"Popped: {lst.pop(-1)}")
    print(lst)
