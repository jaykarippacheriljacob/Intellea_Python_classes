"""
    Runs Per Over Summary
    Easy
    Lists
    Given the list runs with the runs scored in each over, print the list as entered, the runs of the first and last overs, the number of overs, and the three highest scores from highest to lowest. If there are fewer than three overs, print all of them.

    Input Format

    Line 1: number of overs n
    Next n lines: the runs in each over
    Output Format

    Line 1: Runs: <list in entered order>
    Line 2: First over: <runs>
    Line 3: Last over: <runs>
    Line 4: Overs: <count>
    Line 5: Top 3: <list of the highest runs, highest first>
    Examples

    Input: 5 6 12 4 9 15
    Output: Runs: [6, 12, 4, 9, 15] First over: 6 Last over: 15 Overs: 5 Top 3: [15, 12, 9]
    Explanation: Sorted from highest to lowest the list is [15, 12, 9, 6, 4], so the top three are [15, 12, 9].
    Input: 2 8 3
    Output: Runs: [8, 3] First over: 8 Last over: 3 Overs: 2 Top 3: [8, 3]
    Explanation: With only two overs, both are printed in the Top 3 line.
    Constraints

    1 <= n <= 50
    0 <= runs in an over <= 36
    Use list methods, indexing and slicing. Do not use sum(), max(), min() or sorted()
"""

# Read the number of overs
overs = int(input())
# List to store the runs scored in each over
runs_per_over = []
# Read the runs for each over and add them to the list
for i in range(overs):
    runs_per_over.append(int(input()))

# Display all runs, then the first and last over using indexing
print("Runs:", runs_per_over)
print("First over:", runs_per_over[0])
print("Last over:", runs_per_over[-1])
# Display the total number of overs
print("Overs:", overs)
# Sort from highest to lowest so the best overs come first
runs_per_over.sort(reverse = True)
# Slice the first 3 items to get the top 3 overs
print("Top 3:", runs_per_over[:3])

# Test cases: each row is the list of runs per over
test_cases = [
    [4, 10, 2, 7, 12],   # Runs: [4, 10, 2, 7, 12], First: 4, Last: 12, Overs: 5, Top 3: [12, 10, 7]
    [6, 6, 6],           # First: 6, Last: 6, Overs: 3, Top 3: [6, 6, 6]
    [8, 3],              # First: 8, Last: 3, Overs: 2, Top 3: [8, 3]  (fewer than 3 overs)
    [15],                # First: 15, Last: 15, Overs: 1, Top 3: [15]
]

# Run the same steps for each test case
for t, runs in enumerate(test_cases, start=1):
    print(f"\n--- Test {t} ---")
    print("Runs:", runs)
    print("First over:", runs[0])
    print("Last over:", runs[-1])
    print("Overs:", len(runs))
    runs.sort(reverse = True)
    print("Top 3:", runs[:3])
