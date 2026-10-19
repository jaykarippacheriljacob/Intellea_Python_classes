"""
    Electricity Bill Slabs
    Medium
    Conditional Statements
    Given the units of electricity used, print the bill. Each slab is charged at its own rate:

    Units 1 to 100: 3 rupees each.
    Units 101 to 200: 5 rupees each.
    Units above 200: 8 rupees each.
    Input Format

    Line 1: units used
    Output Format

    Line 1: Bill: <total amount>
    Examples

    Input: 80
    Output: Bill: 240
    Explanation: All 80 units are in the first slab. 80 x 3 is 240.
    Input: 250
    Output: Bill: 1200
    Explanation: 100 x 3 + 100 x 5 + 50 x 8 is 1200.
    Constraints

    0 <= units <= 5000
    Use if, elif and else. No loops
"""

# Read the units used
units = int(input())

# Print the label; the amount follows on the same line
print("Bill:", end = " ")
# No units used: bill is 0
if units <= 0:
    print(0)
# Slab 1: units 1 to 100, all at 3 rupees
elif units in range(1, 101):
    print(units * 3)
# Slab 2: first 100 at 3, remaining units at 5
elif units in range(101,201):
    print(100 * 3 + (units - 100) * 5)
# Slab 3: first 100 at 3, next 100 at 5, remaining units at 8
else:
    print(100 * 3 + 100 * 5 + (units - 200)* 8)

# Test cases (written without loops, since the problem doesn't allow them)
# Test 1: 0 units → Bill: 0
print(f"\nTest 1 → Bill: {0}")
# Test 2: 80 units → 80 × 3 = 240
print(f"Test 2 → Bill: {80 * 3}")
# Test 3: 100 units (slab 1 boundary) → 100 × 3 = 300
print(f"Test 3 → Bill: {100 * 3}")
# Test 4: 150 units → 300 + 50 × 5 = 550
print(f"Test 4 → Bill: {100 * 3 + (150 - 100) * 5}")
# Test 5: 200 units (slab 2 boundary) → 300 + 100 × 5 = 800
print(f"Test 5 → Bill: {100 * 3 + (200 - 100) * 5}")
# Test 6: 250 units → 300 + 500 + 50 × 8 = 1200
print(f"Test 6 → Bill: {100 * 3 + 100 * 5 + (250 - 200) * 8}")
