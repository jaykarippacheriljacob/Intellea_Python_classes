"""
    Group Anagrams
    Medium
    Arrays & Hashing
    Given an array of strings strs, group the anagrams together. You can return the answer in any order.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

    Examples

    Arguments: ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    Returns: [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
    Explanation: The strings "eat", "tea", and "ate" are anagrams. The strings "nat" and "tan" are anagrams. The string "bat" has no anagrams in the list.
    Arguments: ['']
    Returns: [[""]]
    Explanation: A single empty string forms its own group.
    Arguments: ['a']
    Returns: [["a"]]
    Explanation: A single-character string forms a group of one.
    Arguments: ['abc', 'def', 'ghi']
    Returns: [["abc"], ["def"], ["ghi"]]
    Explanation: No strings are anagrams of each other, so each forms its own group. The order of the groups in the output does not matter.
    Constraints

    1 <= strs.length <= 10^4
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.
"""
def group_anagrams(strs):
    """
        Group words that are anagrams of each other.

        Parameters:
        strs (list): A list of lowercase strings.

        Returns:
        list: A list of groups, where each group is a list of anagrams.
    """
    # Dictionary to hold groups: key = sorted letters, value = list of words
    groups = {}
    # Iterate through each word in the input list
    for word in strs:
        # Sort the letters and join them back into a string, e.g. "tea" -> "aet"
        key = "".join(sorted(word))
        # First time seeing this key: start a new empty group
        if key not in groups:
            groups[key] = []
        # Add the word to its group
        groups[key].append(word)
    # Sort the words inside each group
    result = []
    for group in groups.values():
        str = sorted(group)
        result.append(str)
    # Sort the groups so the output order is always the same
    result.sort()
    return result

# Example usage
print(group_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
print(group_anagrams(['']))
# Output: [['']]
print(group_anagrams(['a']))
# Output: [['a']]
print(group_anagrams(['abc', 'def', 'ghi']))
# Output: [['abc'], ['def'], ['ghi']]