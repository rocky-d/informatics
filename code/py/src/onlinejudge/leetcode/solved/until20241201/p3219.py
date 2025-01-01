from onlinejudge.leetcode import *


class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        ans = 0
        rows, cols = 1, 1
        for cut, horizontal in sorted(chain(((cut, True) for cut in horizontalCut), ((cut, False) for cut in verticalCut)), key=lambda item: item[0], reverse=True):
            if horizontal:
                rows += 1
                ans += cut * cols
            else:  # if not horizontal:
                cols += 1
                ans += cut * rows
        return ans
