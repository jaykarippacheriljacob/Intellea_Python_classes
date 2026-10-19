"""
    Two Sum
    Easy
    General Programming
    Given a list of integers nums and an integer target, return the indices of the two numbers in the list that add up to the target.

    You may assume that each input has exactly one solution, and you may not use the same element twice.

    The order of the indices in your returned list does not matter.

    Examples

    Arguments: [2, 7, 11, 15] 9
    Returns: [0, 1]
    Explanation: <code>nums[0]</code> (which is 2) + <code>nums[1]</code> (which is 7) equals 9. So, we return their indices <code>[0, 1]</code>.
    Arguments: [3, 2, 4] 6
    Returns: [1, 2]
    Explanation: <code>nums[1]</code> (which is 2) + <code>nums[2]</code> (which is 4) equals 6. So, we return their indices <code>[1, 2]</code>.
    Arguments: [3, 3] 6
    Returns: [0, 1]
    Explanation: The two numbers are at indices 0 and 1. Both have the value 3, and their sum is 6. Even though the values are the same, they are at different positions.
    Constraints

    2 <= len(nums) <= 1000
    -1000 <= nums[i] <= 1000
    -2000 <= target <= 2000
    Exactly one solution is guaranteed to exist.
"""

def two_sum (nums, target):
    """
        Find the indices of two different numbers in the list that add up to the target.

        Parameters:
        nums (list): A list of integers.
        target (int): The sum to look for.

        Returns:
        list: The two indices [a, b] whose values add up to target, or an empty list if no pair exists.
    """
    # Initialize an empty list to hold the matching indices
    indices = []
    # Store the length of the list
    l = len(nums)
    # Pick the first number using index a
    for a in range(l):
        # Pick the second number using index b
        for b in range(l):
            # Skip pairing a number with itself
            if a != b:
                # Add the two numbers together
                sum = nums[a] + nums[b]
                # If the pair matches the target, store both indices and return
                if sum == target:
                    indices.append(a)
                    indices.append(b)
                    return indices
    # Return an empty list if no pair was found
    return indices

# Example usage
print(two_sum([2, 7, 11, 15], 9))   # Output: [0, 1]
print(two_sum([3, 2, 4], 6))        # Output: [1, 2]
print(two_sum([3, 3], 6))           # Output: [0, 1]
print(two_sum([-1, -2, -3, -4], -7))  # Output: [2, 3]
print(two_sum([1, 2, 3], 10))       # Output: []