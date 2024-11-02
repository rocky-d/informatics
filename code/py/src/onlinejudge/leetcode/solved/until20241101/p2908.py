from onlinejudge.leetcode import *


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        pref_min = deque([nums[0]])
        for i in range(1, n - 2, +1):
            pref_min.append(nums[i] if nums[i] < pref_min[-1] else pref_min[-1])
        suff_min = deque([nums[-1]])
        for i in range(n - 2, 1, -1):
            suff_min.appendleft(nums[i] if nums[i] < suff_min[0] else suff_min[0])
        return min((pref + suff + nums[i] for pref, suff, i in zip(pref_min, suff_min, range(1, n - 1)) if pref < nums[i] and suff < nums[i]), default = -1)
