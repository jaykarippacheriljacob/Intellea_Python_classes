"""
    Type Journey of a Number
    Medium
    Variables and Data Types
    Given a whole number read with input(), print the type of the raw value. Convert it to int and print the new type. Then convert that int to float and print the float value and its type.

    Input Format

    Line 1: a whole number
    Output Format

    Line 1: type of the raw input
    Line 2: type after int()
    Line 3: the value after float()
    Line 4: type after float()
    Examples

    Input: 25
    Output: <class 'str'> <class 'int'> 25.0 <class 'float'>
    Explanation: input() gives the string '25'. int() makes it 25 and float() makes it 25.0.
    Constraints

    -100000 <= number <= 100000
    Use only variables, input(), type(), type casting and print()
"""

# Read the input as a string (input() always returns a string)
raw = input()

# Show that the original input is a string
print(type(raw))
# Convert to an integer and show its type
print(type(int(raw)))
# Convert to a decimal number and show the value
print(float(raw))
# Show the type of the converted decimal number
print(type(float(raw)))
