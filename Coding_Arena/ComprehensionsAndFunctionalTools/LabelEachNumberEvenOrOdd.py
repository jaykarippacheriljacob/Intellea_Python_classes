""" 
    Label Each Number Even or Odd
    Easy
    general programming
    Task

    Write a function label_evens_odds(numbers) that returns a new list of strings. For each number, include its index, its value, and whether it is even or odd.

    Format

    Each returned string must have this exact format:

    index:value:label
    where label is even if the number is divisible by 2, otherwise odd.

    Parameters

    Name	Type	Description
    numbers	list of integers	The numbers to label.
    Return value

    Return a list of strings, one for each number in numbers, in the same order.

    Example

    Input:  [3, 4, 7]
    Output: ['0:3:odd', '1:4:even', '2:7:odd']
    Examples

    Arguments: [3, 4, 7]
    Returns: ['0:3:odd', '1:4:even', '2:7:odd']
    Explanation: The first number is odd, the second is even, and the third is odd.
    Arguments: [2, 2, 1]
    Returns: ['0:2:even', '1:2:even', '2:1:odd']
    Explanation: Each item is labeled using its position and whether it is divisible by 2.
    Arguments: []
    Returns: []
    Explanation: An empty list produces an empty list.
    Constraints

    - 0 <= len(numbers) <= 1000
    - Each element of numbers is an integer in the range -10^9 to 10^9   
"""

def label_evens_odds(numbers):
    """Return a list of index:value:label strings for the given numbers."""
    # List to collect the labelled strings
    result = []
    # Index counter for each number's position
    i = 0
    # Labels for even and odd numbers
    e = "even"
    o = "odd"
    for n in numbers:
        # Even number: remainder 0 when divided by 2
        if n%2 == 0:
            result.append(str(i) + ":" + str(n) + ":" + e)
        # Odd number: remainder 1
        else:
            result.append(str(i) + ":" + str(n) + ":" + o)
        # Move to the next index
        i += 1
    return result


# Test cases
print(label_evens_odds([4, 7, 10]))   # Output: ['0:4:even', '1:7:odd', '2:10:even']
print(label_evens_odds([0, -3, -8]))  # Output: ['0:0:even', '1:-3:odd', '2:-8:even']   (zero and negatives)
print(label_evens_odds([5]))          # Output: ['0:5:odd']
print(label_evens_odds([]))           # Output: []
