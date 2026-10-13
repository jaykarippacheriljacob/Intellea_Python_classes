"""
    Perfect Number
    Medium
    General Programming
    Your task is to write a function that determines if a given positive integer is a perfect number.

    A perfect number is a positive integer that is equal to the sum of its proper positive divisors. A proper positive divisor is any positive divisor of a number, other than the number itself.

    For example, the number 6 is a perfect number. Its proper divisors are 1, 2, and 3. The sum of these divisors is 1 + 2 + 3 = 6.

    Task

    Given an integer n, return True if it is a perfect number and False otherwise.

    Examples

    Arguments: 28
    Returns: True
    Explanation: The proper divisors of 28 are 1, 2, 4, 7, and 14. Their sum is 1 + 2 + 4 + 7 + 14 = 28.
    Arguments: 6
    Returns: True
    Explanation: The proper divisors of 6 are 1, 2, and 3. Their sum is 1 + 2 + 3 = 6.
    Arguments: 12
    Returns: False
    Explanation: The proper divisors of 12 are 1, 2, 3, 4, and 6. Their sum is 16, which is not equal to 12.
    Constraints

    1 <= n <= 100000
"""

def is_perfect(n):
    """
    """
    divisors = []
    sum = 0
    for i in range(1,n):
        if n % i == 0:
            divisors.append((i))
            sum += i
    if sum == n:
        return True
    else:
        return False