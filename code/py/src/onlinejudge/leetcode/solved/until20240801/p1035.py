from onlinejudge.leetcode import *


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp0, dp1 = [0] + [0 for _ in nums2], [0] + [0 for _ in nums2]
        for num1 in nums1:
            for j, num2 in enumerate(nums2):
                dp1[j + 1] = dp0[j] + 1 if num1 == num2 else max(dp0[j + 1], dp1[j])
            dp0, dp1 = dp1, dp0
        return dp0[-1]
