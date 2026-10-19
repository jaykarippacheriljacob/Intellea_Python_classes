"""
    Find the Majority Element
    Easy
    General Programming
    Given an array nums of size n, your task is to find and return the majority element.

    The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the array is non-empty and the majority element always exists in the array.

    Examples

    Arguments: [3, 2, 3]
    Returns: 3
    Explanation: The array has a size of 3. The majority element must appear more than ⌊3 / 2⌋ = 1 time. The number 3 appears 2 times, which is more than 1. Therefore, 3 is the majority element.
    Arguments: [2, 2, 1, 1, 1, 2, 2]
    Returns: 2
    Explanation: The array has a size of 7. The majority element must appear more than ⌊7 / 2⌋ = 3 times. The number 2 appears 4 times, which is more than 3. Therefore, 2 is the majority element.
    Arguments: [1]
    Returns: 1
    Explanation: The array has a size of 1. The majority element must appear more than ⌊1 / 2⌋ = 0 times. The number 1 appears 1 time. Therefore, 1 is the majority element.
    Constraints

    Let `n` be the length of `nums`.
    - `1 <= n <= 5 * 10^4`
    - `-10^9 <= nums[i] <= 10^9`
    - The majority element is guaranteed to exist.
"""

def find_majority_element(nums: list[int]) -> int:
    """
        Find the element that appears most often in the list.

        Parameters:
        nums (list): A list of integers.

        Returns:
        int: The element with the highest count.
    """
    # Store the length of the list
    l = len(nums)
    # Dictionary to store how many times each number appears
    count_of_nums = {}
    # Iterate through each number in the list
    for num in nums:
        # Already seen: increase its count
        if num in count_of_nums:
            count_of_nums[num] += 1
        # First time seen: start its count at 1
        else:
            count_of_nums[num] = 1
    # Track the highest count found so far
    max = 0
    # Track the number that has the highest count
    key = 0
    # Iterate through each number and its count
    for k, v in count_of_nums.items():
        # Update when a higher count is found
        if v > max:
            key = k
            max = v
    return key

# Example usage
print(find_majority_element([3, 2, 3]))              # Output: 3
print(find_majority_element([2, 2, 1, 1, 1, 2, 2]))  # Output: 2
print(find_majority_element([1]))                    # Output: 1
print(find_majority_element([5, 5, 5, 4, 4]))        # Output: 5
print(find_majority_element([-1, -1, 7]))            # Output: -1
