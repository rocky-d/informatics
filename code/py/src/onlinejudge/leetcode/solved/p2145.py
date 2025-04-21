from onlinejudge.leetcode import *


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        num = minm = maxm = 0
        for diff in differences:
            num += diff
            minm = min(minm, num)
            maxm = max(maxm, num)
        return max(0, 1 + (upper - lower) - (maxm - minm))
