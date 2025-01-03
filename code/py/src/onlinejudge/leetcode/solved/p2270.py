from onlinejudge.leetcode import *


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefs = list(accumulate(nums, initial=0))
        total = prefs[-1]
        return sum(1 for i in range(1, len(nums)) if total <= prefs[i] + prefs[i])
