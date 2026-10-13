"""
    Harshad Number
    Easy
    General Programming
    An integer is a Harshad number (or Niven number) if it is divisible by the sum of its digits.

    Given a positive integer n, write a function that returns True if it is a Harshad number, and False otherwise.

    Examples

    Arguments: 18
    Returns: True
    Explanation: The sum of the digits is 1 + 8 = 9. Since 18 is divisible by 9 (18 % 9 == 0), it is a Harshad number.
    Arguments: 19
    Returns: False
    Explanation: The sum of the digits is 1 + 9 = 10. Since 19 is not divisible by 10 (19 % 10 != 0), it is not a Harshad number.
    Arguments: 156
    Returns: True
    Explanation: The sum of the digits is 1 + 5 + 6 = 12. Since 156 is divisible by 12 (156 % 12 == 0), it is a Harshad number.
    Constraints

    1 <= n <= 100000
"""

def is_harshad_number(n):
    """
        Check if a given positive integer n is a Harshad number.
    """
    # Convert the integer to a string to easily access its digits
    num = str(n)
    sum = 0
    # Calculate the sum of the digits
    while num:
        sum = sum + int(num[-1])
        num = num[:-1]
    # Check if the sum is a divisor of n
    if n % sum == 0:
        return True
    else:
        return False

n = 156
print(is_harshad_number(n))