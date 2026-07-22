from typing import List

"""
Approach:
    (write your approach here)

Time complexity:  O(?)
Space complexity: O(?)
"""


class Solution:
    def solve(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {num: i for i, num in enumerate(nums)}
        for i, num in enumerate(nums):
            pair = target - num
            if pair in nums_dict:
                j = nums_dict[pair]
                if i != j:
                    return [i, j]

        return []
