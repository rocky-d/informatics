from onlinejudge.leetcode import *


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefs = list(accumulate(nums, initial = 0))
        cnter = Counter(pref % k for pref in prefs)
        return sum(cnter[pref % k] - 1 for pref in prefs) // 2
