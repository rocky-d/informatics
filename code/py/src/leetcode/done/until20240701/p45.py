from rockyutil.leetcode import *


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [i for i in range(n)]
        for i in range(n - 1):
            for j in range(i + 1, min(n, 1 + i + nums[i])):
                dp[j] = min(dp[j], 1 + dp[i])
        return dp[-1]
