"""
    Fibonacci Number
    Easy
    general programming
    The Fibonacci numbers, commonly denoted F(n), form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1.

    The sequence starts as follows:

    0, 1, 1, 2, 3, 5, 8, 13, 21, ...
    Formal Definition

    F(0) = 0
    F(1) = 1
    F(n) = F(n - 1) + F(n - 2), for n > 1.
    Your task is to write a function that, given an integer n, calculates and returns F(n).

    Examples

    Arguments: 2
    Returns: 1
    Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
    Arguments: 3
    Returns: 2
    Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
    Arguments: 4
    Returns: 3
    Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
    Constraints

    0 <= n <= 30
"""

def fib(n: int) -> int:
    """
        Return the nth Fibonacci number.

        Parameters:
        n (int): The position in the Fibonacci sequence (starting from 0).

        Returns:
        int: The nth Fibonacci number.
    """
    # Start with the first two Fibonacci numbers
    a = 0
    b = 1
    # The 0th Fibonacci number is 0
    if n == 0:
        return 0
    # Generate the next numbers until reaching position n
    for i in range(1,n):
        # The next number is the sum of the previous two
        c = a + b
        # Shift both values one step forward
        a = b
        b = c
    # b now holds the nth Fibonacci number
    return b

# Example usage
print(fib(0))    # Output: 0
print(fib(1))    # Output: 1
print(fib(2))    # Output: 1
print(fib(5))    # Output: 5
print(fib(10))   # Output: 55


######
def fib(n: int) -> int:
    """
        Return the nth Fibonacci number using recursion.

        Parameters:
        n (int): The position in the Fibonacci sequence (starting from 0).

        Returns:
        int: The nth Fibonacci number.
    """
    # Base cases: fib(0) = 0, fib(1) = 1
    if n <= 1:
        return n
    # Each number is the sum of the two before it
    return fib(n - 1) + fib(n - 2)

# Example usage
print(fib(0))    # Output: 0
print(fib(1))    # Output: 1
print(fib(2))    # Output: 1
print(fib(5))    # Output: 5
print(fib(10))   # Output: 55