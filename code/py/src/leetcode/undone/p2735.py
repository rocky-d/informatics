from rockyutil.leetcode import *


class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        inf = float("inf")
        ans = inf
        dp = [inf for _ in range(n)]
        for i in range(n):
            for j in range(n):
                dp[j] = min(dp[j], nums[(i + j) % n])
            ans = min(ans, i * x + sum(dp))
        return ans
