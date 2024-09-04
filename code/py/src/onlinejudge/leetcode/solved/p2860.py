from onlinejudge.leetcode import *


class Solution:
    def countWays(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        if 0 < nums[0]:
            ans += 1
        for cnt, (lst, nxt) in enumerate(pairwise(nums), start=1):
            if lst < cnt < nxt:
                ans += 1
        if nums[-1] < len(nums):
            ans += 1
        return ans
