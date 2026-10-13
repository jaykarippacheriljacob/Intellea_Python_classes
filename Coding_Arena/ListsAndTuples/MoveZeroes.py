"""
    Move Zeroes
    Easy
    general programming
    Given a list of integers nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

    Note: You must do this in-place without making a copy of the list. The function should modify the list directly and not return anything.

    Examples

    Arguments: [0, 1, 0, 3, 12]
    Returns: [1, 3, 12, 0, 0]
    Explanation: After the function call, the list `nums` is modified in-place. The non-zero elements 1, 3, and 12 are moved to the front, maintaining their original relative order. The zeroes are moved to the end.
    Arguments: [0]
    Returns: [0]
    Explanation: The list contains only a zero, so it remains unchanged after the operation.
    Arguments: [4, 0, 2, 0, 9]
    Returns: [4, 2, 9, 0, 0]
    Explanation: The non-zero elements 4, 2, and 9 keep their relative order, and the two zeroes are moved to the end of the list.
    Constraints

    1 <= nums.length <= 10^4
    -2^31 <= nums[i] <= 2^31 - 1
"""

def move_zeroes(nums):
    """
        Move all zeros in the list to the end while keeping the order of non-zero elements.

        Parameters:
        nums (list): A list of integers.

        Returns:
        list: The same list with all zeros moved to the end.
    """
    # Initialize a counter for the number of zeros
    count = 0
    # Iterate through the list and count the zeros
    for num in nums:
        if num == 0:
            count += 1
    # Repeat once for every zero found
    while count != 0:
        # Remove the first zero from the list
        nums.remove(0)
        # Add a zero to the end of the list
        nums.append(0)
        # Decrease the remaining zero count
        count -= 1
    return nums

print(move_zeroes([0, 1, 0, 3, 12]))   # Output: [1, 3, 12, 0, 0]
print(move_zeroes([0, 0, 1]))          # Output: [1, 0, 0]
print(move_zeroes([1, 2, 3]))          # Output: [1, 2, 3]
print(move_zeroes([0]))                # Output: [0]