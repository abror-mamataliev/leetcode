"""
Approach:
    (write your approach here)

Time complexity:  O(?)
Space complexity: O(?)
"""


class Solution:
    def solve(self, s: str) -> bool:
        stack = []
        pair = {
            "}": "{",
            ")": "(",
            "]": "[",
        }
        for ch in s:
            if ch in pair.values():
                stack.append(ch)
            elif ch in pair.keys():
                if len(stack) > 0 and stack[-1] == pair[ch]:
                    stack.pop()
                else:
                    return False
        else:
            return False if len(stack) > 0 else True
