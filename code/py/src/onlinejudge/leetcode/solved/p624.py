from onlinejudge.leetcode import *


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        ans = 0
        array = arrays.pop(0)
        minm, maxm = array[0], array[-1]
        for array in arrays:
            a0, a1 = array[0], array[-1]
            ans = max(ans, abs(maxm - a0), abs(a1 - minm))
            minm, maxm = min(minm, a0), max(maxm, a1)
        return ans
