from onlinejudge.leetcode import *


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = 1
        inc, dec = 1, 1
        for lst, nxt in pairwise(nums):
            if lst < nxt:
                dec = 1
                inc += 1
                ans = max(ans, inc)
            elif lst > nxt:
                inc = 1
                dec += 1
                ans = max(ans, dec)
            else:  # elif lst == nxt:
                inc, dec = 1, 1
        return ans
