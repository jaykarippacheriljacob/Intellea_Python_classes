"""
    Mall Parking Fee
    Hard
    Operators
    Given an entry time, an exit time (24 hour clock, same day) and an hourly rate, print the minutes parked, the hours charged, the fee and an overstay warning.

    Any part of an hour is charged as a full hour, so 61 minutes is 2 hours.
    Fee = hours charged x rate.
    The warning is True if the stay is more than 240 minutes or the exit hour is 22 or later.
    Input Format

    Line 1: entry hour
    Line 2: entry minute
    Line 3: exit hour
    Line 4: exit minute
    Line 5: rate per hour
    Output Format

    Line 1: minutes parked
    Line 2: hours charged
    Line 3: fee
    Line 4: True or False for the warning
    Examples

    Input: 9 15 11 40 30
    Output: 145 3 90 False
    Explanation: 9:15 to 11:40 is 145 minutes, which is charged as 3 hours. 3 x 30 is 90.
    Input: 18 0 22 0 20
    Output: 240 4 80 True
    Explanation: 240 minutes is exactly 4 hours and not an overstay, but the exit is at 22:00, so the warning is True.
    Constraints

    0 <= hour <= 23 and 0 <= minute <= 59
    The exit is at least 1 minute after the entry
    1 <= rate <= 500
    Use only operators. No if statements or loops
"""

# Read entry time, exit time and hourly rate
entry_hour = int(input())
entry_minute = int(input())
exit_hour = int(input())
exit_minute = int(input())
rate = int(input())

# Convert both times into total minutes since midnight
entry_in_min = entry_hour * 60 + entry_minute
exit_in_min = exit_hour * 60 + exit_minute

# Total parking duration in minutes
diff = exit_in_min - entry_in_min
# Full hours parked
hr = int(diff / 60)
# Remaining minutes after the full hours
min = diff % 60

# Any leftover minutes count as one more billable hour
if min > 0:
    hr += 1

# Display duration, billable hours and total charge
print(diff)
print(hr)
print(hr * rate)

# Flag: parked longer than 4 hours OR left at 10 PM or later
if diff > 240 or exit_hour >= 22:
    print("True")
else:
    print("False")

# Test cases: [entry_hour, entry_minute, exit_hour, exit_minute, rate]
test_cases = [
    [9, 0, 11, 0, 50],     # Exactly 2 hours → 120, 2, 100, False
    [9, 15, 11, 40, 50],   # 2 h 25 min → 145, 3, 150, False
    [8, 0, 13, 0, 20],     # 5 hours → 300, 5, 100, True
    [20, 30, 22, 0, 30],   # Exits at 22:00 → 90, 2, 60, True
    [10, 0, 14, 0, 40],    # Exactly 4 hours → 240, 4, 160, False
]

# Run the same steps for each test case
for i, (eh, em, xh, xm, r) in enumerate(test_cases, start=1):
    print(f"\n--- Test {i} ---")
    d = (xh * 60 + xm) - (eh * 60 + em)
    h = d // 60
    if d % 60 > 0:
        h += 1
    print(d)
    print(h)
    print(h * r)
    print(d > 240 or xh >= 22)
    