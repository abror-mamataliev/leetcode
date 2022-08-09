from typing import List
from importlib import import_module


log = import_module("utils", "..").log


@log()
def twoSum(nums: List[int], target: int) -> List[int]:
    """
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    Example:
    Given nums = [2, 7, 11, 15], target = 9,
    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].

    :param nums: List[int] - list of integers
    :param target: int - the target sum
    :return: List[int] - list of indices of the two numbers

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def run():
    twoSum(nums=[2, 7, 11, 15], target=9)
    twoSum(nums=[3, 2, 4], target=6)
    twoSum(nums=[3, 3], target=6)
