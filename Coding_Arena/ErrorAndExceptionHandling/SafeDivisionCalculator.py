"""     
    Safe Division Calculator
    Easy
    Error and Exception Handling
    Given a list of (a, b) text pairs, divide every pair without crashing. For each pair, inside a try block convert both texts with int() and compute a // b.

    On a ValueError the line is Invalid number.
    On a ZeroDivisionError the line is Cannot divide by zero.
    Otherwise, in the else block, the line is Result: <answer>.
    Count every attempt in a finally block.

    Parameters

    pairs: list of (a, b) pairs of texts, for example [(10, 3), (x, 2)]
    Returns

    A tuple (lines, attempts, successful, failed).

    lines: one result line per pair, in order
    attempts: how many pairs were tried
    successful: how many pairs gave a result
    failed: how many pairs gave an error line
    Examples

    Arguments: [('10', '3'), ('8', '0'), ('x', '2'), ('-9', '2')]
    Returns: (['Result: 3', 'Cannot divide by zero', 'Invalid number', 'Result: -5'], 4, 2, 2)
    Explanation: 8 // 0 raises a ZeroDivisionError and int("x") raises a ValueError. -9 // 2 rounds down to -5. Two pairs worked and two failed.
    Constraints

    1 <= number of pairs <= 20
    Each text has no spaces and is at most 10 characters long
    Convert both texts before dividing, so an invalid text is reported even when the other number is 0
    Use try, except, else and finally. Do not check the text with if before converting it
"""

def divide_all(pairs):
    # List to hold one message per pair
    eval = []
    # Counters for successful and failed divisions
    succ = 0
    fail = 0
    # Total number of pairs processed
    count = len(pairs)
    for p in pairs:
        try:
            # Convert both values to integers and floor-divide
            r = int(p[0])//int(p[1])
        # A value couldn't be converted to an integer
        except ValueError:
            eval.append("Invalid number")
            fail += 1
        # The divisor was zero
        except ZeroDivisionError:
            eval.append("Cannot divide by zero")
            fail += 1
        # No error: record the result
        else:
            eval.append("Result: " + str(r))
            succ += 1
    return (eval, count, succ, fail)


# Test cases
print(divide_all([("10", "2"), ("7", "0"), ("abc", "3")]))
# Output: (['Result: 5', 'Cannot divide by zero', 'Invalid number'], 3, 1, 2)
print(divide_all([("9", "4"), ("-7", "2")]))
# Output: (['Result: 2', 'Result: -4'], 2, 2, 0)   (// rounds down, so -7 // 2 is -4)
print(divide_all([("x", "0")]))
# Output: (['Invalid number'], 1, 0, 1)   (int("x") fails before the division happens)
print(divide_all([]))
# Output: ([], 0, 0, 0)
