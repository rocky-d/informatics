from rockyutil.leetcode import *


class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        ans = 1_000_000_000_000
        dp = nums.copy()
        for i in range(n):
            for j in range(n):
                dp[j] = min(dp[j], nums[(i + j) % n])
            ans = min(ans, i * x + sum(dp))
        return ans
