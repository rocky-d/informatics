from onlinejudge.leetcode import *


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums2)
        dp = [0] + [0] * n
        for num1 in nums1:
            dp_lst, dp = dp, [0] + [0] * n
            for i, num2 in enumerate(nums2, start = 1):
                dp[i] = dp_lst[i - 1] + 1 if num1 == num2 else max(dp[i - 1], dp_lst[i])
        return dp[-1]
