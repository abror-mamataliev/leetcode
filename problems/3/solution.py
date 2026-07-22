"""
Approach:
    (write your approach here)

Time complexity:  O(?)
Space complexity: O(?)
"""


class Solution:
    def solve(self, s: str) -> int:
        max_length = 0
        substr = set()
        left, right = 0, 0
        for ch in s:
            if ch not in substr:
                substr.add(ch)
                right += 1
            else:
                curr = right - left
                if curr > max_length:
                    max_length = curr

                while left < right:
                    substr.remove(s[left])
                    left += 1
                    if s[left - 1] == ch:
                        substr.add(ch)
                        right += 1
                        break
        else:
            curr = right - left
            if curr > max_length:
                max_length = curr

        return max_length
