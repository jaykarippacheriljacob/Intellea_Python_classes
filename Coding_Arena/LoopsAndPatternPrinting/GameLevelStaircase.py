"""
    Game Level Staircase
    Medium
    For Loops
    Given n, print a staircase of # symbols with n rows that leans to the right. Row i has n - i spaces followed by i # symbols.

    Input Format

    Line 1: number of steps n
    Output Format

    n lines, one for each row. No spaces after the last #.
    Examples

    Input: 4
    Output: # ## ### ####
    Explanation: Row 1 has 3 spaces and 1 #. Row 4 has no spaces and 4 #.
    Constraints

    1 <= n <= 50
    Use nested for loops with range(). Do not use string multiplication
"""

# Read the height of the staircase
n = int(input())

# One row per step, from 1 to n
for i in range(1,n+1):
    # Print leading spaces: n - i of them, to right-align the row
    for j in range(1, n+1-i):
        print(end = " ")
    # Print i hashes for the current row
    for j in range (1,i+1):
        print("#", end = "")
    # Move to the next line
    print()

# Test cases: different staircase heights
test_cases = [1, 3, 5]

# Draw the staircase for each test height
for t, size in enumerate(test_cases, start=1):
    print(f"\n--- Test {t}: n = {size} ---")
    for i in range(1, size+1):
        for j in range(1, size+1-i):
            print(end = " ")
        for j in range(1, i+1):
            print("#", end = "")
        print()
        