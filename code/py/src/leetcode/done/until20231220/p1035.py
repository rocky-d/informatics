from rockyutil.leetcode import *


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp1, dp2 = [0] + [0 for _ in nums2], [0] + [0 for _ in nums2]
        for nums1_i in nums1:
            for j, nums2_j in enumerate(nums2):
                dp2[j + 1] = dp1[j] + 1 if nums1_i == nums2_j else max(dp1[j + 1], dp2[j])
            dp1, dp2 = dp2, dp1
        return dp1[-1]
