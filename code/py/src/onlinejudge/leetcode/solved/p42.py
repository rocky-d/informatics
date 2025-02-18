from onlinejudge.leetcode import *


class Solution:
    def trap(self, height: List[int]) -> int:
        cnt = 0
        hl = 0
        hr = 0
        r = range(len(height))
        for l, r in zip(r, reversed(r)):
            hl = max(hl, height[l])
            hr = max(hr, height[r])
            cnt += hl + hr
        return cnt - hl * len(height) - sum(height)
