from onlinejudge.leetcode import *


class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        dp = []
        for num in nums:
            for i in range(len(dp)):
                dp.append(dp[i] * num)
            dp.append(num)
        return max(dp)
