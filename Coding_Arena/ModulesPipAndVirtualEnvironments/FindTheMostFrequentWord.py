""" 
    Find the Most Frequent Word
    Easy
    general programming
    Task

    Write a function most_common_word(words) that uses the collections module to find the most frequent word in a list of strings.

    Parameters

    Parameter	Type	Description
    words	list of strings	The words to analyze.
    Return value

    If words is not empty, return a dictionary with exactly these keys: "word" and "count".
    "word" should be the most frequent word.
    "count" should be how many times that word appears.
    If the list is empty, return None.
    Rules

    Words are case-sensitive.
    No punctuation needs to be removed.
    If there is a tie for most frequent word, return any one of the tied words.
    Examples

    Arguments: ["apple", "banana", "apple", "cherry", "apple", "banana"]
    Returns: {"word": "apple", "count": 3}
    Explanation: "apple" appears 3 times, which is more than any other word.
    Arguments: ["red", "blue", "red", "blue"]
    Returns: {"word": "red", "count": 2}
    Explanation: "red" and "blue" are tied, so returning either one with count 2 is acceptable.
    Arguments: ["Cat", "cat", "cat", "dog"]
    Returns: {"word": "cat", "count": 2}
    Explanation: The comparison is case-sensitive, so "cat" and "Cat" are different words.
    Constraints

    - 0 <= len(words)
    - Each element of words is a plain string.
    - Strings are case-sensitive.
    - No punctuation stripping is required. 
"""

def most_common_word(words):
    """Return the most frequent word and its count, or None if the list is empty."""
    # Dictionary to count how many times each word appears
    dict = {}
    # Holds the current most frequent word and its count
    result = {"word":"", "count":0} 
    for word in words:
        # Note: this line has no effect, since the lowered string isn't stored
        word.lower()
        # First time seen: start its count at 1
        if word not in dict:
            dict[word] = 1
        # Already seen: add one more
        else:
            dict[word] += 1
    # Find the word with the highest count; on a tie, the first one stays
    for k,v in dict.items():
        if result["count"] < v:
            result["word"] = k
            result["count"] = v
    return result


# Test cases
print(most_common_word(["apple", "banana", "apple", "cherry", "apple", "banana"]))
# Output: {'word': 'apple', 'count': 3}
print(most_common_word(["red", "blue", "red", "blue"]))
# Output: {'word': 'red', 'count': 2}   (tie → first one seen)
print(most_common_word(["Cat", "cat", "cat", "dog"]))
# Output: {'word': 'cat', 'count': 2}   (case-sensitive)
print(most_common_word(["solo"]))
# Output: {'word': 'solo', 'count': 1}
print(most_common_word([]))
# Expected: None
# Your code returns: {'word': '', 'count': 0}

