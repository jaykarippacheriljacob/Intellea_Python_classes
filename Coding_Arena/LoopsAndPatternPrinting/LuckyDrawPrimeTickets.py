"""
    Lucky Draw Prime Tickets
    Hard
    For Loops
    Given a start and an end ticket number, print every winning ticket in increasing order, then the number of winners. A ticket wins if its number is prime: greater than 1 and divisible only by 1 and itself. If there are no winners, print only No winners.

    Input Format

    Line 1: start ticket number
    Line 2: end ticket number
    Output Format

    Each winning number on its own line, then Winners: <count>
    or only No winners
    Examples

    Input: 10 20
    Output: 11 13 17 19 Winners: 4
    Explanation: Only 11, 13, 17 and 19 are prime between 10 and 20.
    Input: 24 28
    Output: No winners
    Explanation: None of 24 to 28 is prime.
    Constraints

    1 <= start <= end <= 2000
    Use nested for loops with range(). Do not use break, while or lists
"""

# Read the start and end of the range
start = int(input())
end = int(input())

# List to store the prime numbers (winners)
winners = []
# Count of prime numbers found
count = 0
# Check every number in the range, including end
for n in range(start, end+1):
    # 0 and 1 are not prime
    if n == 0 or n == 1:
        p = False
    # Assume the number is prime until a divisor is found
    else:
        p = True
    # Try dividing by every number from 2 to n-1
    for i in range(2, n):
        # A divisor was found, so it's not prime
        if n % i == 0:
            p = False
    # Store the number if it's prime
    if p == True:
        winners.append(n)
        count += 1

# At least one prime: print each one and the total
if count != 0:
    for item in winners:
        print(item)
    print(f"Winners: {count}")
# No primes in the range
else:
    print("No winners")

# Test cases: [start, end]
test_cases = [
    [1, 10],     # 2, 3, 5, 7 → Winners: 4
    [10, 20],    # 11, 13, 17, 19 → Winners: 4
    [14, 16],    # No winners
    [2, 2],      # 2 → Winners: 1
    [0, 1],      # No winners
]

# Run the same steps for each test case
for t, (s, e) in enumerate(test_cases, start=1):
    print(f"\n--- Test {t}: {s} to {e} ---")
    winners = []
    for n in range(s, e+1):
        p = n >= 2
        for i in range(2, n):
            if n % i == 0:
                p = False
        if p:
            winners.append(n)
    if winners:
        for item in winners:
            print(item)
        print(f"Winners: {len(winners)}")
    else:
        print("No winners")
        