from onlinejudge.leetcode import *


class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        ans = 0
        rows, cols = 1, 1
        for cut, direction in sorted(
                chain(((cut, True) for cut in horizontalCut), ((cut, False) for cut in verticalCut)),
                key = lambda item: item[0], reverse = True):
            if True is direction:
                ans += cut * cols
                rows += 1
            else:
                ans += cut * rows
                cols += 1
        return ans
