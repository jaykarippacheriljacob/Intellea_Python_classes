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
        Check whether a number is a perfect number.

        Parameters:
        n (int): A positive integer to check.

        Returns:
        bool: True if n is a perfect number, False otherwise.
    """
    # Initialize an empty list to hold the proper divisors of n
    divisors = []
    # Initialize the running sum of divisors
    sum = 0
    # Iterate through every number from 1 up to n-1
    for i in range(1,n):
        # Check if i divides n evenly
        if n % i == 0:
            # Store the divisor and add it to the sum
            divisors.append((i))
            sum += i
    # A perfect number equals the sum of its proper divisors
    if sum == n:
        return True
    else:
        return False

n = 19
print(is_perfect(n))
n = 28
print(is_perfect(n))