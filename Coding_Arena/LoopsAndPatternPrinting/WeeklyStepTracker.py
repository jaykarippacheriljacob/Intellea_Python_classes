"""
    Weekly Step Tracker
    Easy
    For Loops
    Given the step counts for n days, print the total steps and the number of goal days. A goal day has 10000 steps or more.

    Input Format

    Line 1: number of days n
    Next n lines: the steps for each day
    Output Format

    Line 1: Total steps: <total>
    Line 2: Goal days: <count>
    Examples

    Input: 5 8000 12000 10000 4500 15000
    Output: Total steps: 49500 Goal days: 3
    Explanation: The total is 49500. Three days have 10000 steps or more.
    Constraints

    1 <= n <= 365
    0 <= steps <= 100000
    Use a for loop with range(). Do not use lists
"""

# Read the number of days
n = int(input())

# Running total of all steps
total = 0
# Count of days where the 10000-step goal was reached
goal = 0
# Read the steps for each day
for i in range(0,n):
    steps = int(input())
    # Add the day's steps to the total
    total += steps
    # Count the day if the goal was reached
    if steps >= 10000:
        goal += 1
# Display the results
print(f"Total steps: {total}")
print(f"Goal days: {goal}")

# Test cases: each row is the list of daily steps
test_cases = [
    [8000, 12000, 10000],   # Total: 30000, Goal days: 2
    [5000, 6000, 7000],     # Total: 18000, Goal days: 0
    [15000],                # Total: 15000, Goal days: 1
    [9999, 10000, 10001],   # Total: 30000, Goal days: 2 (boundary)
    [],                     # Total: 0, Goal days: 0 (n = 0)
]

# Run the same steps for each test case
for i, days in enumerate(test_cases, start=1):
    print(f"\n--- Test {i} ---")
    total = 0
    goal = 0
    for steps in days:
        total += steps
        if steps >= 10000:
            goal += 1
    print(f"Total steps: {total}")
    print(f"Goal days: {goal}")
    