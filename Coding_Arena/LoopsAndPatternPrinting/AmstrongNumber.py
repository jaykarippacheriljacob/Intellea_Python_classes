"""
    Armstrong Number
    Easy
    general programming
    Given a non-negative integer n, write a function to determine if it is an Armstrong number.

    An Armstrong number (also known as a narcissistic number) is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

    How it works:

    First, count the number of digits in the integer. Let's call this count d.
    Next, for each digit in the number, calculate that digit raised to the power of d.
    Finally, sum up all these results.
    If the final sum is equal to the original number n, then n is an Armstrong number.
    For example, take the number 153:

    It has 3 digits.
    The sum of its digits raised to the power of 3 is: 1³ + 5³ + 3³.
    This equals 1 + 125 + 27 = 153.
    Since the result (153) is the same as the original number, 153 is an Armstrong number.
    Examples

    Arguments: 153
    Returns: True
    Explanation: 153 has 3 digits. The sum of the cubes of its digits is 1³ + 5³ + 3³ = 1 + 125 + 27 = 153. Since the sum equals the original number, it's an Armstrong number.
    Arguments: 1634
    Returns: True
    Explanation: 1634 has 4 digits. The sum of its digits to the power of 4 is 1⁴ + 6⁴ + 3⁴ + 4⁴ = 1 + 1296 + 81 + 256 = 1634. This equals the original number.
    Arguments: 10
    Returns: False
    Explanation: 10 has 2 digits. The sum of the squares of its digits is 1² + 0² = 1 + 0 = 1. Since 1 is not equal to 10, it is not an Armstrong number.
    Constraints

    The input `n` will be a non-negative integer.
    `0 <= n <= 2 * 10^9`
"""

def is_armstrong(n: int) -> bool:
    """
        Determine if a number n is an Armstrong number.
    """
    # Count the number of digits in n
    l = len(str(n))
    # Convert the number to a string to iterate over its digits
    num = str(n)
    sum = 0
    # Calculate the sum of each digit raised to the power of the number of digits
    while num:
        sum = sum + int(num[-1])**l
        num = num[:-1]
    # Check if the sum is equal to the original number
    if sum == n:
        return True
    else:
       return False

n = 153
print(is_armstrong(n))
n = 1634
print(is_armstrong(n))
n = 10
print(is_armstrong(n))