from onlinejudge.leetcode import *


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        prefs = list(accumulate(nums, initial=0))
        div = prefs[-1] % p
        if 0 == div:
            return 0
        ans = n = len(nums)
        lst = {}
        for idx, pref in enumerate(prefs):
            lst[pref % p] = idx
            ans = min(ans, idx - lst.get((pref - div) % p, -n))
        return ans if ans < n else -1
