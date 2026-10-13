"""
    Add Two Numbers
    Easy
    Math
    Read two integers a and b from standard input (separated by a space on a single line) and print their sum.

    Examples

    Input: 2 3
    Output: 5
    Explanation: 2 + 3 = 5
    Input: 10 20
    Output: 30
    Explanation: 10 + 20 = 30
    Input: -5 5
    Output: 0
    Explanation: -5 + 5 = 0
    Input: 1000000 2000000
    Output: 3000000
    Explanation: handles large values
    Constraints

    -10^9 <= a, b <= 10^9
"""

# Read the input and split it into two parts
string = input().split(" ")
# Alternatively, you can use map to convert the input directly to integers
# a, b = map(int, input().split(" "))

# Convert the string inputs to integers and calculate their sum
a = int(string[0])
b = int(string[1])
c = a+b

# Print the result
print(c)