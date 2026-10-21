"""
    Student Report Functions
    Medium
    Functions Fundamentals
    Implement four functions.

    calculate_stats(m1, m2, m3) returns two values: the total and the average, which is total // 3.
    get_grade(average) returns A for 90 or more, B for 75 or more, C for 50 or more, and F otherwise.
    has_passed(m1, m2, m3, pass_mark=35) returns True if every mark is at least pass_mark.
    final_status(m1, m2, m3, pass_mark=35) returns Pass with grade <grade> if the student passed and the grade is not F, and Fail otherwise. It calls the other three functions.
    The function student_report is already written. It uses your functions.

    Parameters

    name: student name
    m1: first mark
    m2: second mark
    m3: third mark
    Returns

    A list [name, total, average, grade, status, strict_status] given by student_report: the name, the total, the average, the grade, the status with pass mark 35 and the status with pass mark 50.

    Examples

    Arguments: 'Asha' 92 88 95
    Returns: ['Asha', 275, 91, 'A', 'Pass with grade A', 'Pass with grade A']
    Explanation: 275 // 3 = 91, which is grade A, and every mark is above both pass marks.
    Arguments: 'Ravi' 80 45 70
    Returns: ['Ravi', 195, 65, 'C', 'Pass with grade C', 'Fail']
    Explanation: All marks reach 35, but 45 is below the strict pass mark of 50.
    Constraints

    0 <= mark <= 100
    Return the results. Do not print inside the functions
"""

def calculate_stats(m1, m2, m3):
    # Return the total of the three marks and the floored average
    return m1+m2+m3, (m1+m2+m3)//3


def get_grade(average):
    # Grade A: average 90 or more
    if average >= 90:
        return "A"
    # Grade B: average 75 or more
    elif average >= 75:
        return "B"
    # Grade C: average 50 or more
    elif average >= 50:
        return "C"
    # Grade F: anything below 50
    else:
        return "F"


def has_passed(m1, m2, m3, pass_mark=35):
    # Passed only if every mark reaches the pass mark (default 35)
    if m1 >= pass_mark and m2 >= pass_mark and m3 >= pass_mark:
        return True
    else:
        return False


def final_status(m1, m2, m3, pass_mark=35):
    # Get the average and convert it to a grade
    tol, avg = calculate_stats(m1, m2, m3)
    grade = get_grade(avg)
    # Check whether all marks reach the pass mark
    passed = has_passed(m1, m2, m3, pass_mark)
    # Pass only if all marks pass AND the grade isn't F
    if passed and grade != "F":
        return "Pass with grade " + grade
    else:
        return "Fail"

# Do not change the code below
def student_report(name, m1, m2, m3):
    total, average = calculate_stats(m1, m2, m3)
    grade = get_grade(average)
    status = final_status(m1, m2, m3)
    strict = final_status(m1, m2, m3, pass_mark=50)
    return [name, total, average, grade, status, strict]


# Test cases
print(student_report('Asha', 92, 88, 95))
# Output: ['Asha', 275, 91, 'A', 'Pass with grade A', 'Pass with grade A']
print(student_report('Ravi', 80, 45, 70))
# Output: ['Ravi', 195, 65, 'C', 'Pass with grade C', 'Fail']
print(student_report('Meera', 40, 40, 40))
# Output: ['Meera', 120, 40, 'F', 'Fail', 'Fail']   (passes 35 but grade is F)
print(student_report('Arun', 100, 90, 30))
# Output: ['Arun', 220, 73, 'C', 'Fail', 'Fail']    (30 is below 35)
print(student_report('Priya', 90, 89, 91))
# Output: ['Priya', 270, 90, 'A', 'Pass with grade A', 'Pass with grade A']   (exact A boundary)
print(student_report('Kumar', 75, 74, 76))
# Output: ['Kumar', 225, 75, 'B', 'Pass with grade B', 'Pass with grade B']   (exact B boundary)

