"""
    Cinema Entry Gate
    Medium
    Operators
    Given a visitor's age, ticket status and seat row, print three True or False values in this order:

    Entry: age is 18 or more and the ticket is yes.
    Discount: age is below 12, or 60 or more.
    Front row: the row is A, B or C.
    Input Format

    Line 1: age
    Line 2: ticket status (yes or no)
    Line 3: seat row (one capital letter)
    Output Format

    Line 1: entry result
    Line 2: discount result
    Line 3: front row result
    Examples

    Input: 25 yes B
    Output: True False True
    Explanation: 25 with a ticket can enter. 25 gets no discount. B is a front row.
    Input: 65 no K
    Output: False True False
    Explanation: No ticket, so no entry. 65 gets a discount. K is not a front row.
    Constraints

    1 <= age <= 100
    Ticket status is yes or no in lowercase
    Seat row is a capital letter from A to Z
    Use only comparison, logical and membership operators. No if statements
"""

# Read the visitor's age, ticket status and seat row
age = int(input())
ticket = input()
row = input()

# Entry: age must be 18 or more AND the ticket must be "yes"
if age >= 18 and ticket == "yes":
    print("True")
else:
    print("False")
# Discount: age below 12 OR age 60 or more
if age < 12 or age >=60:
    print("True")
else:
    print("False")
# Front row: the row must be A, B or C
if row in ('A', 'B', 'C'):   
    print("True")
else:
    print("False")

# Test cases: [age, ticket, row], as if typed as input
test_cases = [
    [25, "yes", "B"],   # Expected: True, False, True
    [65, "no", "K"],    # Expected: False, True, False
    [10, "yes", "A"],   # Expected: False, True, True
    [18, "yes", "C"],   # Expected: True, False, True
    [60, "yes", "D"],   # Expected: True, True, False
]

# Run the same checks for each test case
for i, (age, ticket, row) in enumerate(test_cases, start=1):
    print(f"\n--- Test {i}: {age}, {ticket}, {row} ---")
    print(age >= 18 and ticket == "yes")
    print(age < 12 or age >= 60)
    print(row in ('A', 'B', 'C'))