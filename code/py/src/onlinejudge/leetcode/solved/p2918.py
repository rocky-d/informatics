from onlinejudge.leetcode import *


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        zeros1 = nums1.count(0)
        zeros2 = nums2.count(0)
        if 0 == zeros1 == zeros2:
            return sum1 if sum1 == sum2 else -1
        if 0 == zeros1:
            return sum1 if sum2 + zeros2 <= sum1 else -1
        if 0 == zeros2:
            return sum2 if sum1 + zeros1 <= sum2 else -1
        return max(sum1 + zeros1, sum2 + zeros2)
