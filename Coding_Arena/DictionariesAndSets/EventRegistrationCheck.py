"""     
    Event Registration Check
    Easy
    Sets
    Given a list names that may contain repeats and a name query, use a set to find the unique names. Count the unique people and the duplicate entries (entries minus unique people), get the unique names as a sorted list, and check whether query is registered.

    Parameters

    names: list of registered names, repeats allowed
    query: name to check
    Returns

    A tuple (unique_count, duplicates, sorted_names, registered):

    unique_count: number of unique people
    duplicates: number of duplicate entries
    sorted_names: list of the unique names in sorted order
    registered: True if query is registered, else False
    Examples

    Arguments: ['Asha', 'Ravi', 'Asha', 'Meena', 'Dev', 'Ravi'] 'Meena'
    Returns: (4, 2, ['Asha', 'Dev', 'Meena', 'Ravi'], True)
    Explanation: Asha and Ravi appear twice, so 4 unique names remain and 2 entries are duplicates.
    Arguments: ['Zoya', 'Zoya', 'Zoya'] 'Asha'
    Returns: (1, 2, ['Zoya'], False)
    Explanation: All three entries are Zoya. Asha is not in the set, so registered is False.
    Constraints

    1 <= len(names) <= 100
    Names have only letters and no spaces and are case sensitive
    Use a set. Do not use sorted()
"""

def check_registrations(names, query):
    # Set removes duplicate names
    unique = set(names)
    # Convert to a list and sort alphabetically, since sets have no order
    unique_l = list(unique)
    unique_l.sort()
    result = []
    # Number of unique names
    result.append(len(unique))
    # Number of duplicate entries (total entries minus unique ones)
    result.append(len(names) - len(unique))
    # Sorted list of unique names
    result.append(unique_l)
    # Whether the query name is registered
    if query in unique:
        result.append(True)
    else:
        result.append(False)
    return tuple(result)


# Test cases
print(check_registrations(["Ravi", "Asha", "Ravi", "Meena", "Asha"], "Meena"))
# Output: (3, 2, ['Asha', 'Meena', 'Ravi'], True)
print(check_registrations(["Ravi", "Asha"], "Arun"))
# Output: (2, 0, ['Asha', 'Ravi'], False)
print(check_registrations(["Ravi", "Ravi", "Ravi"], "ravi"))
# Output: (1, 2, ['Ravi'], False)   (check is case-sensitive)
print(check_registrations([], "Ravi"))
# Output: (0, 0, [], False)

