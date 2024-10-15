from onlinejudge.leetcode import *


class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def func(mid: int) -> int:
            x = (1 + (mid if 0b1 == 0b1 & mid else mid - 1)) * ((mid + 1) // 2) // 2
            y = (2 + (mid if 0b0 == 0b1 & mid else mid - 1)) * (mid // 2) // 2
            return 0 if x <= red and y <= blue or x <= blue and y <= red else 1

        return bisect_left(range(1, 21), 1, key=func)
