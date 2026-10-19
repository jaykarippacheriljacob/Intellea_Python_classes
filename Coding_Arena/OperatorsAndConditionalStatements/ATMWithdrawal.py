"""
    ATM Withdrawal
    Easy
    Conditional Statements
    Given an account balance and a withdrawal amount, print the ATM result. The ATM gives only 100 rupee notes.

    If the amount is not a multiple of 100, print Invalid amount.
    Else if the amount is more than the balance, print Insufficient balance.
    Otherwise print Collect your cash and the new balance.
    Input Format

    Line 1: account balance
    Line 2: withdrawal amount
    Output Format

    Invalid amount
    or Insufficient balance
    or Collect your cash, then Balance: <remaining balance> on the next line
    Examples

    Input: 5000 2000
    Output: Collect your cash Balance: 3000
    Explanation: 2000 is a multiple of 100 and not more than 5000, so 3000 is left.
    Input: 5000 2050
    Output: Invalid amount
    Explanation: 2050 % 100 is 50, so it is not a multiple of 100.
    Constraints

    0 <= balance <= 1000000
    1 <= amount <= 1000000
    Use if, elif and else. No loops
"""

# Read the account balance and the withdrawal amount
balance = int(input())
amount = int(input())

# The ATM only dispenses multiples of 100
if amount % 100 != 0:
    print("Invalid amount")
# Withdrawal can't be more than the available balance
elif amount > balance:
    print("Insufficient balance")
# Valid withdrawal: dispense cash and show the remaining balance
else:
    print("Collect your cash")
    print(f"Balance: {balance-amount}")

# Test cases: [balance, amount]
test_cases = [
    [5000, 2000],   # Valid → Collect your cash, Balance: 3000
    [5000, 2050],   # Not a multiple of 100 → Invalid amount
    [1000, 1500],   # More than balance → Insufficient balance
    [1000, 1000],   # Exactly the balance → Collect your cash, Balance: 0
    [500, 750],     # Invalid AND too much → Invalid amount (checked first)
]

# Run the same checks for each test case
for i, (b, a) in enumerate(test_cases, start=1):
    print(f"\n--- Test {i}: balance {b}, amount {a} ---")
    if a % 100 != 0:
        print("Invalid amount")
    elif a > b:
        print("Insufficient balance")
    else:
        print("Collect your cash")
        print(f"Balance: {b-a}")
        