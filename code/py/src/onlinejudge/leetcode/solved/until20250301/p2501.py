from onlinejudge.leetcode import *


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        maxm = -1
        dp = defaultdict(lambda: 0)
        for num in sorted(nums, reverse=True):
            dp[num] = dp[num * num] + 1
            maxm = max(maxm, dp[num])
        return -1 if 1 == maxm else maxm


eg_nums = [4, 3, 6, 16, 8, 2]
print(Solution().longestSquareStreak(eg_nums))
