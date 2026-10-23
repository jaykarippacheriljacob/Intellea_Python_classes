"""     
    Library Desk Register
    Hard
    Dictionaries
    Given register, mapping each title to {total: copies, issued: 0}, and commands, a list of (action, title, copies) tuples, run each command in order. Available copies are total minus issued.

    ISSUE: fails if the title is missing or no copy is available, else issued rises by 1.
    RETURN: fails if the title is missing or issued is 0, else issued drops by 1.
    ADD: adds copies to total, or adds a new title with issued 0.
    Parameters

    register: dictionary of title to {total: copies, issued: copies}
    commands: list of (action, title, copies) tuples; copies is only used by ADD
    Returns

    A tuple (results, register, out_of_stock):

    results: one message per command, in order: Issued: <title> (available: <n>), Returned: <title> (available: <n>), Added: <title> (total: <n>), Updated: <title> (total: <n>), Unknown book: <title>, No copies left: <title> or Nothing to return: <title>
    register: the final dictionary, in order (new titles at the end)
    out_of_stock: list of titles with no copy available, in register order
    Examples

    Arguments: {'Python': {'total': 2, 'issued': 0}, 'Java': {'total': 1, 'issued': 0}, 'SQL': {'total': 3, 'issued': 0}} [('ISSUE', 'Java', 0), ('ISSUE', 'Java', 0), ('RETURN', 'SQL', 0), ('ADD', 'Go', 4), ('ISSUE', 'Rust', 0), ('ADD', 'Python', 3)]
    Returns: (['Issued: Java (available: 0)', 'No copies left: Java', 'Nothing to return: SQL', 'Added: Go (total: 4)', 'Unknown book: Rust', 'Updated: Python (total: 5)'], {'Python': {'total': 5, 'issued': 0}, 'Java': {'total': 1, 'issued': 1}, 'SQL': {'total': 3, 'issued': 0}, 'Go': {'total': 4, 'issued': 0}}, ['Java'])
    Explanation: Java has 1 copy, so the second ISSUE fails. Go is new, and Python gets 3 more copies. Only Java ends with no copy available.
    Constraints

    1 <= len(register) <= 10 and 1 <= len(commands) <= 30
    0 <= copies <= 100
    Titles have only letters and no spaces and are case sensitive
    Use a nested dictionary
"""

def run_desk(register, commands):
    # List to collect one message per command
    results = []

    for action, title, copies in commands:
        # ISSUE: lend out one copy if the title exists and a copy is available
        if action == "ISSUE":
            if title not in register:
                results.append(f"Unknown book: {title}")
            elif register[title]["total"] - register[title]["issued"] == 0:
                results.append(f"No copies left: {title}")
            else:
                register[title]["issued"] += 1
                available = register[title]["total"] - register[title]["issued"]
                results.append(f"Issued: {title} (available: {available})")

        # RETURN: take back one copy if the title exists and something was issued
        elif action == "RETURN":
            if title not in register:
                results.append(f"Unknown book: {title}")
            elif register[title]["issued"] == 0:
                results.append(f"Nothing to return: {title}")
            else:
                register[title]["issued"] -= 1
                available = register[title]["total"] - register[title]["issued"]
                results.append(f"Returned: {title} (available: {available})")

        # ADD: increase copies of an existing title, or add a new one
        elif action == "ADD":
            if title in register:
                register[title]["total"] += copies
                results.append(f"Updated: {title} (total: {register[title]['total']})")
            else:
                register[title] = {"total": copies, "issued": 0}
                results.append(f"Added: {title} (total: {copies})")

    # Titles with no copy available, in register order
    out_of_stock = []
    for title, info in register.items():
        if info["total"] - info["issued"] == 0:
            out_of_stock.append(title)

    return (results, register, out_of_stock)


# Test case
register = {'Python': {'total': 2, 'issued': 0}, 'Java': {'total': 1, 'issued': 0}, 'SQL': {'total': 3, 'issued': 0}}
commands = [('ISSUE', 'Java', 0), ('ISSUE', 'Java', 0), ('RETURN', 'SQL', 0), ('ADD', 'Go', 4), ('ISSUE', 'Rust', 0), ('ADD', 'Python', 3)]
print(run_desk(register, commands))
# Output: (['Issued: Java (available: 0)', 'No copies left: Java', 'Nothing to return: SQL',
#           'Added: Go (total: 4)', 'Unknown book: Rust', 'Updated: Python (total: 5)'],
#          {'Python': {'total': 5, 'issued': 0}, 'Java': {'total': 1, 'issued': 1},
#           'SQL': {'total': 3, 'issued': 0}, 'Go': {'total': 4, 'issued': 0}},
#          ['Java'])
