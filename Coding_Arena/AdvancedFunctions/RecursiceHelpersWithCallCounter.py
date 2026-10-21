"""
    Recursive Helpers with Call Counter
    Medium
    Advanced Functions
    Write two recursive functions.

    digit_sum(n) returns the sum of the digits of n. If n is less than 10, return n. Otherwise return the last digit plus digit_sum(n // 10).
    power(base, exp) returns base to the power exp without using **. power(base, 0) is 1. Otherwise return base * power(base, exp - 1).
    Every call of either function, including each recursive call, must add 1 to the global variable calls.

    The function recursion_report is already written. It calls digit_sum, then power, and reads calls.

    Parameters

    n: number whose digits are added
    base: base of the power
    exp: exponent of the power
    Returns

    A list [digit_sum, power, calls]: the digit sum of n, base raised to exp, and the total number of calls of both functions.

    Examples

    Arguments: 12345 2 10
    Returns: [15, 1024, 16]
    Explanation: digit_sum runs 5 times, once per digit. power runs 11 times, for exp 10 down to 0. 5 + 11 = 16.
    Arguments: 7 5 0
    Returns: [7, 1, 2]
    Explanation: Each function runs once and makes no recursive call.
    Constraints

    0 <= n <= 1000000000
    -10 <= base <= 10
    0 <= exp <= 50
    Use recursion. Do not use loops or ** inside digit_sum and power
    Use the global keyword for the calls counter
"""

# Global counter that tracks how many times the recursive functions are called
calls = 0


def digit_sum(n):
    # Use the global counter instead of creating a local one
    global calls
    # Count this call
    calls += 1
    # Base case: a single digit is its own digit sum
    if n <= 9:
        return n
    # Recursive case: last digit plus the digit sum of the remaining digits
    return (n % 10) + digit_sum(n // 10)


def power(base, exp):
    # Use the global counter instead of creating a local one
    global calls
    # Count this call
    calls += 1
    # Base case: any number to the power 0 is 1
    if exp == 0:
        return 1
    # Recursive case: base^exp = base × base^(exp-1)
    return base * power(base, exp - 1)


# Do not change the code below
def recursion_report(n, base, exp):
    digits = digit_sum(n)
    result = power(base, exp)
    return [digits, result, calls]


# Test cases (calls is reset before each one, since it's a global that keeps adding up)
calls = 0
print(recursion_report(1234, 2, 5))   # Output: [10, 32, 10]   (4 digit calls + 6 power calls)
calls = 0
print(recursion_report(7, 3, 0))      # Output: [7, 1, 2]      (1 + 1 calls)
calls = 0
print(recursion_report(999, 5, 3))    # Output: [27, 125, 7]   (3 + 4 calls)
calls = 0
print(recursion_report(0, 10, 2))     # Output: [0, 100, 4]    (1 + 3 calls)
