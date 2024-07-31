from rockyutil.leetcode import *


class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        dp = [-inf, -inf]
        num = nums.pop(0)
        parity = 0b1 & num
        dp[parity] = num
        for num in nums:
            parity = 0b1 & num
            dp[parity] = max(dp[parity] + num, dp[parity - 1] + num - x)
        return max(dp)
