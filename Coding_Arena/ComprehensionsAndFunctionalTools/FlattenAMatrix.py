"""     
    Flatten a Matrix
    Easy
    general programming
    Flatten a Matrix

    Write a function named flatten_matrix that takes a 2D list called matrix and returns a new 1D list containing all of its elements in row-by-row order.

    Function signature

    flatten_matrix(matrix)
    Requirements

    Visit the rows from top to bottom.
    Within each row, keep the elements in their original order.
    Return the flattened list.
    Example

    Input:  [[1, 2, 3], [4, 5], [6]]
    Output: [1, 2, 3, 4, 5, 6]
    Examples

    Arguments: [[1, 2, 3], [4, 5], [6]]
    Returns: [1, 2, 3, 4, 5, 6]
    Explanation: The elements are returned in the same order they appear across the rows.
    Arguments: [[7, 8], [9, 10]]
    Returns: [7, 8, 9, 10]
    Explanation: All values from both rows are combined into one list.
    Arguments: [[], [1], [], [2, 3]]
    Returns: [1, 2, 3]
    Explanation: Empty rows contribute no elements to the result.
    Constraints

    0 <= len(matrix) <= 100
    Each row in matrix is a list of integers.
    0 <= sum(len(row) for row in matrix) <= 1000
"""

def flatten_matrix(matrix):
    """Return a flattened 1D list containing all elements of matrix."""
    # List to collect every element in order
    result = []
    # Go through each row of the matrix
    for row in matrix:
        # Go through each element in the current row
        for elem in row:
            # Add the element to the flat list
            result.append(elem)
    return result


# Test cases
print(flatten_matrix([[1, 2, 3], [4, 5, 6]]))   # Output: [1, 2, 3, 4, 5, 6]
print(flatten_matrix([[1, 2], [3], [4, 5, 6]]))  # Output: [1, 2, 3, 4, 5, 6]   (rows of different lengths)
print(flatten_matrix([[7]]))                     # Output: [7]
print(flatten_matrix([[], [1, 2], []]))          # Output: [1, 2]               (empty rows)
print(flatten_matrix([]))                        # Output: []
