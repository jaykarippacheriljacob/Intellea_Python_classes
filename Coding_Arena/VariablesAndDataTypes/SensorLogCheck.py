"""
    Sensor Log Check
    Hard
    Variables and Data Types
    Given a temperature, an operator note and an alert count, all read as text, print four values: the temperature as an int with the decimal part dropped, bool() of the alert count as a number, bool() of the alert count as text, and bool() of the note. The note may be empty.

    Input Format

    Line 1: temperature (a whole or decimal number)
    Line 2: operator note (may be empty)
    Line 3: alert count (a whole number)
    Output Format

    Line 1: temperature as an int
    Line 2: bool of the alert count as a number
    Line 3: bool of the alert count as text
    Line 4: bool of the operator note
    Examples

    Input: 36.7 0
    Output: 36 False True False
    Explanation: int() drops the decimal part, so 36.7 gives 36. The number 0 is False, but the text '0' is not empty, so it is True.
    Input: 98.6 ok 5
    Output: 98 True True True
    Explanation: 5 is not zero, and both '5' and 'ok' are not empty.
    Constraints

    -100.0 <= temperature <= 200.0
    0 <= alert count <= 1000
    Use only variables, input(), type casting and print()
"""

# Read all inputs as strings
temperature = input()
note = input()
alert_count = input()

# Convert temperature to float first, then to int (drops the decimal part)
print(int(float(temperature)))
# Convert alert_count to int, then to bool: 0 is False, any other number is True
print(bool(int(alert_count)))
# bool of the string itself: any non-empty string is True, even "0"
print(bool(alert_count))
# bool of the note: True if something was typed, False if left empty
print(bool(note))
