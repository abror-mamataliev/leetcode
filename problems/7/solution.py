"""
Approach:
    (write your approach here)

Time complexity:  O(?)
Space complexity: O(?)
"""


class Solution:
    def solve(self, x: int) -> int:
        if x == 0:
            return 0
        
        minimum, maximum = str(2**31), str(2**31 - 1)
        is_positive = x > 0
        x_str = str(x)
        if not is_positive:
            x_str = x_str[1:]
        
        if len(x_str) < 10:
            x_reversed_str = x_str[::-1]
        else:
            x_reversed_str = x_str[::-1]
            for i in range(len(x_reversed_str)):
                if (
                        is_positive and x_reversed_str[i] < maximum[i]
                        or
                        not is_positive and x_reversed_str[i] < minimum[i]
                    ):
                    break
                elif (
                        is_positive and x_reversed_str[i] > maximum[i]
                        or
                        not is_positive and x_reversed_str[i] > minimum[i]
                    ):
                    x_reversed_str = 0
                    break
            
        x_reversed = int(x_reversed_str)
        return x_reversed if is_positive else -x_reversed
