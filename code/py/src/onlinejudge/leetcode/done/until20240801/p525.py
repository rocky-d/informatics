from onlinejudge.leetcode import *


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ans = 0
        pref = 0
        prefs_idxes = {pref: 0}
        for idx, num in enumerate(nums, 1):
            pref += -1 if 0 == num else 1
            if pref in prefs_idxes:
                ans = max(ans, idx - prefs_idxes[pref])
            else:
                prefs_idxes[pref] = idx
        return ans
