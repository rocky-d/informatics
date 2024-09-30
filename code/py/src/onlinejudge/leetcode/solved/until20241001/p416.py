from onlinejudge.leetcode import *


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if 0b1 == 0b1 & total:
            return False
        total //= 2
        dp = [0 for _ in range(1 + total)]
        for num in nums:
            for vol in range(total, num - 1, -1):
                dp[vol] = max(dp[vol], dp[vol - num] + num)
        return total == dp[-1]
