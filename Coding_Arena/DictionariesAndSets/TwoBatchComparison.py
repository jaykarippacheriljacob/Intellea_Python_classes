"""     
    Two Batch Comparison
    Medium
    Sets
    Given the names in a Python batch and an SQL batch, use set operations to find the students in both batches, only in Python, and only in SQL, each as a sorted list. Also count the different students and the students who joined exactly one batch. A name repeated inside one batch is one student.

    Parameters

    python_names: list of names in the Python batch
    sql_names: list of names in the SQL batch
    Returns

    A tuple (both, only_python, only_sql, total, exactly_one):

    both, only_python, only_sql: sorted lists of names
    total: number of different students
    exactly_one: number of students in exactly one batch
    Examples

    Arguments: ['Asha', 'Ravi', 'Meena', 'Dev'] ['Ravi', 'Kiran', 'Dev', 'Zoya', 'Zoya']
    Returns: (['Dev', 'Ravi'], ['Asha', 'Meena'], ['Kiran', 'Zoya'], 6, 4)
    Explanation: Dev and Ravi are in both. The union has 6 students and 4 of them are in only one batch.
    Arguments: ['Amar'] ['Bina']
    Returns: ([], ['Amar'], ['Bina'], 2, 2)
    Explanation: The batches share no student, so both is an empty list.
    Constraints

    1 <= len of each list <= 30
    Names have only letters and no spaces and are case sensitive
    Use the set operators &, -, | and ^. Do not use sorted() 
"""

def compare_batches(python_names, sql_names):
    # Convert both lists to sets to remove duplicates
    s_py = set(python_names)
    s_sql = set(sql_names)
    # Students in both batches
    both = list(s_py.intersection(s_sql))
    # Students only in the Python batch
    only_py = list(s_py.difference(s_sql))
    # Students only in the SQL batch
    only_sql = list(s_sql.difference(s_py))
    # Students attending exactly one class
    one_class = len(only_py) + len(only_sql)
    # Total distinct students across both batches
    total_stu = len(s_py.union(s_sql))
    # Sort each list in place (on separate lines, since sort() returns None)
    both.sort()
    only_py.sort()
    only_sql.sort()
    result = [both, only_py, only_sql, total_stu, one_class]
    return tuple(result)


# Test cases
print(compare_batches(['Asha', 'Ravi', 'Meena', 'Dev'], ['Ravi', 'Kiran', 'Dev', 'Zoya', 'Zoya']))
# Output: (['Dev', 'Ravi'], ['Asha', 'Meena'], ['Kiran', 'Zoya'], 6, 4)
print(compare_batches(['Asha', 'Ravi'], ['Asha', 'Ravi']))
# Output: (['Asha', 'Ravi'], [], [], 2, 0)   (same students in both)
print(compare_batches(['Asha'], ['Kiran']))
# Output: ([], ['Asha'], ['Kiran'], 2, 2)    (no overlap)
