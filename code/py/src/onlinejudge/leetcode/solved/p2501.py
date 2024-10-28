from onlinejudge.leetcode import *


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        maxm = -1
        dp = {}
        for num in sorted(nums, reverse=True):
            num_sq = num * num
            if num_sq in dp.keys():
                dp[num] = dp[num_sq] + 1
                maxm = max(maxm, dp[num])
            elif num == isqrt(num) ** 2:
                dp[num] = 1
        return -1 if 1 == maxm else maxm


eg_nums = [4, 3, 6, 16, 8, 2]
print(Solution().longestSquareStreak(eg_nums))
