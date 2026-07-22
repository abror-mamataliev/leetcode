"""
Approach:
    (write your approach here)

Time complexity:  O(?)
Space complexity: O(?)
"""


class Solution:
    def solve(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        table = [["" for _ in range(len(s))] for _ in range(numRows)]
        x, y = 0, 0
        dx, dy = 0, 0
        for ch in s:
            table[y][x] = ch
            if y == 0:
                dx, dy = 0, 1
            elif y == numRows - 1:
                dx, dy = 1, -1

            x += dx
            y += dy

        return "".join(["".join(row) for row in table])
