from importlib import import_module
from typing import List


log = import_module("utils", "..").log


@log
def longestCommonPrefix(strs: List[str]) -> str:
    """
    Given an array of strings, find the longest common prefix.

    Example:
    Input: ["flower","flow","flight"]
    Output: "fl"

    Input: ["dog","racecar","car"]
    Output: ""

    :param strs: List[str] - the array of strings to find the longest common prefix
    :return: str - the longest common prefix

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    pass


def run():
    longestCommonPrefix(strs=["flower", "flow", "flight"])
    longestCommonPrefix(strs=["dog", "racecar", "car"])
