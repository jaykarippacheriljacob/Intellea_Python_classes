"""
    Pizza Party Sharing
    Easy
    Operators
    Given a number of pizza slices and a number of friends, share the slices equally. Print how many whole slices each friend gets and how many slices are left over.

    Input Format

    Line 1: total slices
    Line 2: number of friends
    Output Format

    Line 1: Each friend gets: <slices per friend>
    Line 2: Slices left: <leftover slices>
    Examples

    Input: 17 5
    Output: Each friend gets: 3 Slices left: 2
    Explanation: 17 // 5 is 3 and 17 % 5 is 2.
    Input: 24 6
    Output: Each friend gets: 4 Slices left: 0
    Explanation: 24 shares evenly among 6, so nothing is left.
    Constraints

    0 <= slices <= 1000
    1 <= friends <= 100
    Use only arithmetic operators. No if or loops
"""

# Read the total slices and the number of friends
slices = int(input())
friends = int(input())

# Floor division gives the whole slices each friend gets
spf = slices // friends
# Modulus gives the slices left over after sharing equally
slo = slices % friends
# Display the results
print(f"Each friend gets: {spf}")
print(f"Slices left: {slo}")

# Test cases (written without loops, since the problem doesn't allow them)
# Test 1: 17 slices, 5 friends → 3 each, 2 left
print(f"\nTest 1 → Each friend gets: {17 // 5}, Slices left: {17 % 5}")
# Test 2: 24 slices, 6 friends → 4 each, 0 left
print(f"Test 2 → Each friend gets: {24 // 6}, Slices left: {24 % 6}")
# Test 3: 0 slices, 4 friends → 0 each, 0 left
print(f"Test 3 → Each friend gets: {0 // 4}, Slices left: {0 % 4}")
# Test 4: 3 slices, 8 friends → 0 each, 3 left
print(f"Test 4 → Each friend gets: {3 // 8}, Slices left: {3 % 8}")
