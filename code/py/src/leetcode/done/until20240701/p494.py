from rockyutil.leetcode import *


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if target < -total or +total < target:
            return 0
        total2 = total << 1
        dp = [1] + [0 for _ in range(total2)]
        for num in nums:
            num2 = num << 1
            for vol in range(total2, num2 - 1, -1):
                dp[vol] += dp[vol - num2]
        return dp[total + target]
