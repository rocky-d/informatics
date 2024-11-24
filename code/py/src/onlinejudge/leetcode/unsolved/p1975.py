from onlinejudge.leetcode import *


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        ans = 0
        cnt = 0
        minm = inf
        for row in matrix:
            for val in row:
                if val < 0:
                    cnt += 1
                    val = -val
                minm = min(minm, val)
                ans += val
        if 0b1 == 0b1 & cnt:
            ans -= minm
        return ans
