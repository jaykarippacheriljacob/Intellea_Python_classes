"""
    Personal Loan Approval
    Hard
    Conditional Statements
    Given an applicant's age, monthly income, credit score and existing loan status, decide the loan. Run the checks in this order and stop at the first one that fails:

    Age below 21 or above 60: print Rejected: age
    Income below 15000: print Rejected: income
    Credit score below 650: print Rejected: credit score
    If all pass, print Approved and a loan limit of income x multiplier:

    No existing loan: 20 if the score is 750 or more, else 12.
    Existing loan: 10 if the score is 750 or more, else 5.
    Input Format

    Line 1: age
    Line 2: monthly income
    Line 3: credit score
    Line 4: existing loan (yes or no)
    Output Format

    Rejected: age
    or Rejected: income
    or Rejected: credit score
    or Approved, then Loan limit: <amount> on the next line
    Examples

    Input: 30 50000 780 no
    Output: Approved Loan limit: 1000000
    Explanation: All checks pass. No existing loan and a score of 750 or more gives 50000 x 20.
    Input: 65 90000 800 no
    Output: Rejected: age
    Explanation: 65 is above 60, so the first check fails.
    Constraints

    1 <= age <= 100
    0 <= income <= 10000000
    300 <= credit score <= 900
    Existing loan is yes or no in lowercase
    Use if, elif, else and nested conditions. No loops
"""

# Read the applicant's details
age = int(input())
income = int(input())
score = int(input())
existing_loan = input()

# Age must be between 21 and 60
if age < 21 or age > 60:
    print("Rejected: age")
# Monthly income must be at least 15000
elif income < 15000:
    print("Rejected: income")
# Credit score must be at least 650
elif score < 650:
    print("Rejected: credit score")
# All checks passed: approve and calculate the loan limit
else:
    print("Approved")
    print("Loan limit:", end = " ")
    # Applicant already has a loan: lower multipliers
    if existing_loan.lower() == "yes":
        # Excellent score: 10 × income, otherwise 5 × income
        if score >=750:
            print(income * 10)
        else:
            print(income * 5)
    # No existing loan: higher multipliers
    else:
        # Excellent score: 20 × income, otherwise 12 × income
        if score >=750:
            print(income * 20)
        else:
            print(income * 12)

# Test cases: [age, income, score, existing_loan]
test_cases = [
    [19, 30000, 800, "no"],    # Rejected: age
    [30, 12000, 800, "no"],    # Rejected: income
    [30, 30000, 600, "no"],    # Rejected: credit score
    [30, 30000, 780, "no"],    # Approved, Loan limit: 600000
    [30, 30000, 700, "no"],    # Approved, Loan limit: 360000
    [45, 20000, 760, "yes"],   # Approved, Loan limit: 200000
    [45, 20000, 680, "Yes"],   # Approved, Loan limit: 100000
    [60, 15000, 650, "no"],    # Boundaries → Approved, Loan limit: 180000
]

# Run the same checks for each test case
for i, (a, inc, s, loan) in enumerate(test_cases, start=1):
    print(f"\n--- Test {i} ---")
    if a < 21 or a > 60:
        print("Rejected: age")
    elif inc < 15000:
        print("Rejected: income")
    elif s < 650:
        print("Rejected: credit score")
    else:
        print("Approved")
        print("Loan limit:", end = " ")
        if loan.lower() == "yes":
            print(inc * 10 if s >= 750 else inc * 5)
        else:
            print(inc * 20 if s >= 750 else inc * 12)
            