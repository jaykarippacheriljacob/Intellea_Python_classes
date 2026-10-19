"""
    Verifying an Alien Dictionary
    Easy
    general programming
    Problem

    In an alien language, the lowercase English letters appear in a different order.

    You are given:

    a list of words written in that language, and
    a string order that gives the alphabet order as a permutation of all 26 lowercase English letters.
    Return true if and only if the words are sorted in lexicographical order according to this alien alphabet.

    Lexicographical rules

    Compare two words character by character from left to right.
    The first position where the two words differ determines their order.
    If one word is a prefix of the other, the shorter word comes first.
    Function

    Write a function isAlienSorted(words, order) that returns a boolean value.

    Parameter	Type	Description
    words	List[str]	The sequence of words to check.
    order	str	The alien alphabet order.
    Return value

    Return True if the list is sorted in alien lexicographical order, otherwise return False.

    Examples

    Arguments: ["hello", "leetcode"] "hlabcdefgijkmnopqrstuvwxyz"
    Returns: True
    Explanation: The first letters compare as 'h' before 'l' in the given order, so the list is sorted.
    Arguments: ["word", "world", "row"] "worldabcefghijkmnpqstuvxyz"
    Returns: False
    Explanation: The first two words are out of order because the first differing letters are 'd' and 'l', and 'd' comes after 'l' in the given order.
    Arguments: ["apple", "app"] "abcdefghijklmnopqrstuvwxyz"
    Returns: False
    Explanation: The second word is a prefix of the first, so the shorter word should come first.
    Constraints

    1 <= words.length <= 100
    1 <= words[i].length <= 20
    order.length == 26
    All characters in words[i] and order are lowercase English letters.
"""

