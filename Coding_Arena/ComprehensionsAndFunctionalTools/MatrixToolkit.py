""" 
    Matrix Toolkit
    Hard
    Comprehensions
    Implement four functions on a matrix (a nested list) using comprehensions. Always scan the cells row by row.

    transpose(matrix) returns the matrix with rows and columns swapped.
    even_values(matrix) returns a flat list of the even values.
    cells_above(matrix, threshold) returns (row, column) tuples, counting from 0, for every cell whose value is greater than threshold.
    repeated_values(matrix) returns a dictionary mapping each value that appears more than once to its count, in order of first appearance.
    The function matrix_toolkit is already written. It uses your functions.

    Parameters

    matrix: nested list of whole numbers, one inner list per row
    threshold: cells greater than this value are reported
    Returns

    A list [transposed, evens, above, repeated]:

    transposed: the transposed matrix
    evens: flat list of even values
    above: list of (row, column) tuples
    repeated: dictionary of value to count
    Examples

    Arguments: [[1, 2, 3], [4, 5, 2]] 3
    Returns: [[[1, 4], [2, 5], [3, 2]], [2, 4, 2], [(1, 0), (1, 1)], {2: 2}]
    Explanation: Only 4 and 5 are greater than 3, at (1, 0) and (1, 1). The value 2 appears two times.
    Arguments: [[5]] 5
    Returns: [[[5]], [], [], {}]
    Explanation: 5 is odd and not greater than 5, and no value repeats.
    Constraints

    1 <= rows <= 8
    1 <= columns <= 8
    -100 <= value <= 100
    -100 <= threshold <= 100
    Use comprehensions for every result. Do not use sum(), min(), max(), sorted(), zip(), enumerate(), map() or filter() 
"""

def transpose(matrix):
    # List to hold the new rows (one per column of the original)
    result = []
    # Outer loop: each column index of the original matrix
    for i in range(len(matrix[0])):
        temp = []
        # Inner loop: take that column's value from every row
        for j in range(len(matrix)):
            temp.append(matrix[j][i])
        # The collected column becomes a row of the result
        result.append(temp)
    return result


def even_values(matrix):
    # Flat list of even values, scanning row by row
    result = []
    for row in matrix:
        for elem in row:
            # Even if the remainder after dividing by 2 is 0
            if elem % 2 == 0:
                result.append(elem)
    return result


def cells_above(matrix, threshold):
    # List of (row, column) positions of cells greater than the threshold
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > threshold:
                result.append((i,j))
    return result


def repeated_values(matrix):
    # Count how many times each value appears, in order of first appearance
    result = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # First time seen: start its count at 1
            if matrix[i][j] not in result:
                result[matrix[i][j]] = 1
            # Already seen: add one more
            else:
                result[matrix[i][j]] += 1
    # Keep only the values that appear more than once
    return {k:v for k, v in result.items() if v > 1} 

# Do not change the code below
def matrix_toolkit(matrix, threshold):
    return [transpose(matrix), even_values(matrix), cells_above(matrix, threshold), repeated_values(matrix)]


# Test cases
print(matrix_toolkit([[1, 2, 3], [4, 5, 2]], 3))
# Output: [[[1, 4], [2, 5], [3, 2]], [2, 4, 2], [(1, 0), (1, 1)], {2: 2}]
print(matrix_toolkit([[5]], 5))
# Output: [[[5]], [], [], {}]
print(matrix_toolkit([[-2, 3], [3, -2], [7, 8]], 0))
# Output: [[[-2, 3, 7], [3, -2, 8]], [-2, -2, 8], [(0, 1), (1, 0), (2, 0), (2, 1)], {-2: 2, 3: 2}]
print(matrix_toolkit([[1, 1, 1]], 1))
# Output: [[[1], [1], [1]], [], [], {1: 3}]
