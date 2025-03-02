from onlinejudge.leetcode import *


class Solution:
    def trap(self, height: List[int]) -> int:
        cnt = 0
        h = 0
        for hi in height:
            h = max(h, hi)
            cnt += h
        h = 0
        for hi in reversed(height):
            h = max(h, hi)
            cnt += h
        return cnt - h * len(height) - sum(height)
