"""
    Number of Ways to Form a Target String
    Easy
    general programming
    You are given a list of strings words, where every string has the same length, and a string target.

    Form target from left to right. For each character of target, you may choose a matching character from any string in words at some column index. After choosing a character from column k, all characters in column 0 through k become unavailable for every string.

    Return the number of different ways to form target. Since the answer may be large, return it modulo 10^9 + 7.

    Function Signature

    Implement the function count_ways(words, target).

    Parameters

    Name	Type	Description
    words	List[str]	A list of strings of equal length.
    target	str	The string to form.
    Return Value

    Return an integer: the number of ways to form target, modulo 10^9 + 7.

    Rules

    You must form target from left to right.
    For each chosen character, you may use any string in words.
    Once a column is used, that column and all columns to its left can no longer be used.
    Multiple characters may come from the same string, as long as the column rule is satisfied.
    Examples

    Arguments: ["acca", "bbbb", "caca"] "aba"
    Returns: 6
    Explanation: There are 6 valid ways to choose columns and matching characters to form the target.
    Arguments: ["abba", "baab"] "bab"
    Returns: 4
    Explanation: There are 4 valid ways to form the target using the available columns.
    Arguments: ["abc", "abc", "abc"] "abc"
    Returns: 27
    Explanation: Each character can be chosen from any of the 3 strings at its matching column, giving 3 choices for each of the 3 positions.
    Constraints

    1 <= len(words) <= 1000
    1 <= len(words[i]) <= 1000
    All strings in words have the same length.
    1 <= len(target) <= 1000
"""

