from onlinejudge.leetcode import *


class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        diffs = [0] * max(hi for _, hi in nums)
        diffs_len = len(diffs)
        for lo, hi in nums:
            diffs[lo - 1] += 1
            if hi < diffs_len:
                diffs[hi] -= 1
        return sum(1 for pref in accumulate(diffs, initial=0) if 0 < pref)
