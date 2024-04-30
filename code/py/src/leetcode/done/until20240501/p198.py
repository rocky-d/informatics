from rockyutil.leetcode import *


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp0, dp1 = 0, 0
        for num in nums:
            dp0, dp1 = dp1, max(dp1, dp0 + num)
        return dp1
