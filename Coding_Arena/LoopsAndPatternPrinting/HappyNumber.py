"""
    Happy Number
    Easy
    general programming
    Write a function to determine if a number n is a "happy number".

    A happy number is a number defined by the following process:

    Starting with any positive integer, replace the number by the sum of the squares of its digits.
    Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy.
    Return True if n is a happy number, and False if not.

    Examples

    Arguments: 19
    Returns: True
    Explanation: The process is as follows: 1² + 9² = 1 + 81 = 82 8² + 2² = 64 + 4 = 68 6² + 8² = 36 + 64 = 100 1² + 0² + 0² = 1 + 0 + 0 = 1 Since the process ends in 1, 19 is a happy number.
    Arguments: 2
    Returns: False
    Explanation: The process enters a cycle that does not include 1: 2 → 2² = 4 4 → 4² = 16 16 → 1² + 6² = 37 37 → 3² + 7² = 58 58 → 5² + 8² = 89 89 → 8² + 9² = 145 145 → 1² + 4² + 5² = 42 42 → 4² + 2² = 20 20 → 2² + 0² = 4 Since the number 4 has appeared again, we are in a cycle (4 → 16 → ... → 4) and will never reach 1.
    Arguments: 7
    Returns: True
    Explanation: The process for 7 is: 7 → 7² = 49 49 → 4² + 9² = 16 + 81 = 97 97 → 9² + 7² = 81 + 49 = 130 130 → 1² + 3² + 0² = 1 + 9 + 0 = 10 10 → 1² + 0² = 1 + 0 = 1 Since the process ends in 1, 7 is a happy number.
    Constraints

    1 <= n <= 2^31 - 1
"""

def is_happy(n: int) -> bool:
   """
    Determine if a number n is a happy number.
   """

   seen = set()  # To keep track of numbers we've seen to detect cycles
   # Loop until we reach 1 or a number less than or equal to 9
   while True:
    
    # Convert the number to a string to iterate over its digits
    num = str(n)

    # Calculate the sum of the squares of the digits
    sum = 0
    while num:
        sum = sum + int(num[-1])**2
        num = num[:-1]
    if sum == 1:
        return True
    # Check if we've seen this sum before (cycle detection)
    elif sum in seen:
        return False
    else:
        n = sum
        seen.add(sum)

n = 11
print(is_happy(n))