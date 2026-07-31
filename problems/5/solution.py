"""
Approach:
    (write your approach here)

Time complexity:  O(?)
Space complexity: O(?)
"""


class Solution:
    def solve(self, s: str) -> str:
        lengths = []
        for _ in s:
            lengths.append(1)
            lengths.append(0)

        for i in range(len(s)):
            distance = 1
            while i - distance >= 0 and i + distance < len(s):
                if s[i - distance] != s[i + distance]:
                    break

                distance += 1
                lengths[2 * i] += 2

            distance = 0
            while i - distance >= 0 and i + 1 + distance < len(s):
                if s[i - distance] != s[i + 1 + distance]:
                    break

                distance += 1
                lengths[2 * i + 1] += 2

        i = sorted(range(len(lengths)), key=lambda x: lengths[x], reverse=True)[0]
        if i % 2 == 0:
            left = i // 2 - (lengths[i] - 1) // 2
            return s[left:left + lengths[i]]
        else:
            left = (i - 1) // 2 - lengths[i] // 2 + 1
            return s[left:left + lengths[i]]
