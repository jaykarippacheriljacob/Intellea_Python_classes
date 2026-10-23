"""         
    Result Sheet Builder
    Medium
    Comprehensions
    Implement four functions using comprehensions. Keep the input order of students everywhere.

    build_results(names, marks) returns a dictionary mapping names[i] to marks[i].
    grade_sheet(results) returns a dictionary mapping each name to Pass if the mark is 40 or more, otherwise Fail.
    distinction_list(results) returns the names with a mark of 75 or more.
    add_grace(results) returns a dictionary mapping each name to its mark plus 5. A mark never goes above 100.
    The function result_sheet is already written. It uses your functions.

    Parameters

    names: list of student names
    marks: list of marks, in the same order as names
    Returns

    A list [results, grades, distinction, bonus]:

    results: dictionary of name to mark
    grades: dictionary of name to Pass or Fail
    distinction: list of names with 75 or more
    bonus: dictionary of name to mark after the grace marks
    Examples

    Arguments: ['Asha', 'Ravi', 'Meena', 'Dev'] [92, 38, 75, 100]
    Returns: [{'Asha': 92, 'Ravi': 38, 'Meena': 75, 'Dev': 100}, {'Asha': 'Pass', 'Ravi': 'Fail', 'Meena': 'Pass', 'Dev': 'Pass'}, ['Asha', 'Meena', 'Dev'], {'Asha': 97, 'Ravi': 43, 'Meena': 80, 'Dev': 100}]
    Explanation: Ravi has 38, so he fails. Asha, Meena and Dev have 75 or more. Dev already has 100, so his bonus mark stays 100.
    Constraints

    1 <= number of students <= 30
    Names have only letters and no spaces, and all names are different
    0 <= mark <= 100
    Use dictionary and list comprehensions. Do not use zip(), min(), max(), sorted() or enumerate() 
"""

def build_results(names, marks):
    # Map each name to the mark at the same index
    return {names[i]:marks[i] for i in range(len(names))} 


def grade_sheet(results):
    # Pass if the mark is 40 or more, otherwise Fail
    return {k: "Pass" if m >= 40 else "Fail" for k, m in results.items()}


def distinction_list(results):
    # Keep only the names with 75 or more
    return [k for k, m in results.items() if m >= 75]


def add_grace(results):
    # Add 5 grace marks, capped at 100
    return {k: m+5 if m+5 <=100 else 100 for k, m in results.items()}


# Do not change the code below
def result_sheet(names, marks):
    results = build_results(names, marks)
    return [results, grade_sheet(results), distinction_list(results), add_grace(results)]


# Test cases
print(result_sheet(['Asha', 'Ravi', 'Meena', 'Dev'], [92, 38, 75, 100]))
# Output: [{'Asha': 92, 'Ravi': 38, 'Meena': 75, 'Dev': 100},
#          {'Asha': 'Pass', 'Ravi': 'Fail', 'Meena': 'Pass', 'Dev': 'Pass'},
#          ['Asha', 'Meena', 'Dev'],
#          {'Asha': 97, 'Ravi': 43, 'Meena': 80, 'Dev': 100}]
print(result_sheet(['Kiran', 'Zoya'], [97, 40]))
# Output: [{'Kiran': 97, 'Zoya': 40}, {'Kiran': 'Pass', 'Zoya': 'Pass'},
#          ['Kiran'], {'Kiran': 100, 'Zoya': 45}]   (97 capped at 100; 40 is exactly a pass)
print(result_sheet(['Arun'], [0]))
# Output: [{'Arun': 0}, {'Arun': 'Fail'}, [], {'Arun': 5}]

