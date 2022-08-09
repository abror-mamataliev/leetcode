from importlib import import_module


log = import_module("utils", "..").log


@log
def lengthOfLongestSubstring(s: str) -> int:
    """
    Given a string, find the length of the longest substring without repeating characters.

    Example:
    Input: "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

    Input: "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

    Input: "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

    :param s: str - the string to find the length of the longest substring without repeating characters
    :return: int - the length of the longest substring without repeating characters

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    pass


def run():
    lengthOfLongestSubstring(s="abcabcbb")
    lengthOfLongestSubstring(s="bbbbb")
    lengthOfLongestSubstring(s="pwwkew")
