"""     
    Marks Entry Validator
    Medium
    Error and Exception Handling
    Implement the functions below to check typed marks.

    validate_mark(text) returns the text as an int. Use raise ValueError(Mark must be a number) when int() fails, and raise ValueError(Mark must be between 0 and 100) when the number is below 0 or above 100.
    check_entries(entries) calls validate_mark on each entry inside a try block. On a ValueError the line is Rejected '<entry>': <message>. Otherwise, in the else block, the line is Accepted: <mark> and the mark is kept. Count each entry in a finally block. Return (lines, valid marks, entries checked).
    average(marks) returns sum // count, or the text none when the list is empty.
    The function check_marks is already written. It uses your functions.

    Parameters

    entries: list of typed entries, each a text without spaces
    Returns

    A list [lines, valid, avg, checked] given by check_marks.

    lines: one Accepted or Rejected line per entry
    valid: the list of valid marks
    avg: the average of the valid marks, or none
    checked: how many entries were checked
    Examples

    Arguments: ['85', 'abc', '101', '-3', '100']
    Returns: [['Accepted: 85', "Rejected 'abc': Mark must be a number", "Rejected '101': Mark must be between 0 and 100", "Rejected '-3': Mark must be between 0 and 100", 'Accepted: 100'], [85, 100], 92, 5]
    Explanation: abc is not a number. 101 and -3 are out of range. The average is 185 // 2 = 92.
    Arguments: ['x', '7.5']
    Returns: [["Rejected 'x': Mark must be a number", "Rejected '7.5': Mark must be a number"], [], 'none', 2]
    Explanation: int("7.5") raises a ValueError, and with no valid marks the average is "none".
    Constraints

    1 <= number of entries <= 20
    Each entry has between 1 and 10 characters and no spaces
    Use raise inside validate_mark. The error messages must match exactly
    Return the results. Do not print inside the functions
"""

def validate_mark(text):
    # Convert the text to an int; replace Python's message with the required one
    try:
        mark = int(text)
    except ValueError:
        raise ValueError("Mark must be a number")
    # Reject marks outside the 0-100 range
    if mark > 100 or mark < 0:
        raise ValueError("Mark must be between 0 and 100")
    return mark

def check_entries(entries):
    # Lines for each entry, the valid marks, and the number of entries checked
    result = []
    valid = []
    checked = 0
    for e in entries:
        try:
            # Validate the entry; raises ValueError if it's invalid
            v = validate_mark(e)
        # Invalid entry: show the entry in quotes and the error message
        except ValueError as ve:
            result.append("Rejected '" + e + "': "+ str(ve))
        # Valid entry: record the line and keep the mark
        else:
            result.append("Accepted: "+ str(v))
            valid.append(v)
        # Runs for every entry, valid or not
        finally:
            checked += 1
    return (result, valid, checked)

def average(marks):
    # No valid marks: return the text "none"
    if len(marks) == 0:
        return "none"
    else:
        # Add up all the marks
        s = 0
        l = len(marks)
        for m in marks:
            s += m
        # Floor division gives a whole-number average
        s = s//l
        return s


# Do not change the code below
def check_marks(entries):
    lines, valid, checked = check_entries(entries)
    return [lines, valid, average(valid), checked]


# Test cases
print(check_marks(['85', 'abc', '101', '-3', '100']))
# Output: [['Accepted: 85', "Rejected 'abc': Mark must be a number",
#           "Rejected '101': Mark must be between 0 and 100",
#           "Rejected '-3': Mark must be between 0 and 100", 'Accepted: 100'], [85, 100], 92, 5]
print(check_marks(['x', '7.5']))
# Output: [["Rejected 'x': Mark must be a number", "Rejected '7.5': Mark must be a number"], [], 'none', 2]
print(check_marks(['0', '100', '50']))
# Output: [['Accepted: 0', 'Accepted: 100', 'Accepted: 50'], [0, 100, 50], 50, 3]   (both boundaries accepted)
print(check_marks(['007', '+40']))
# Output: [['Accepted: 7', 'Accepted: 40'], [7, 40], 23, 2]   (int() handles leading zeros and a + sign)
