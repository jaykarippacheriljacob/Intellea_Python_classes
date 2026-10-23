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


