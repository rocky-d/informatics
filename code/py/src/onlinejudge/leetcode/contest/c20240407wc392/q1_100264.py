from onlinejudge.leetcode import *


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc, dec = 1, 1
        cnt1, cnt2 = 1, 1
        for lst, nxt in pairwise(nums):
            if lst < nxt:
                cnt1 += 1
                cnt2 = 1
                inc = max(inc, cnt1)
            elif nxt < lst:
                cnt2 += 1
                cnt1 = 1
                dec = max(dec, cnt2)
            else:
                cnt1 = 1
                cnt2 = 1
        return max(inc, dec)
