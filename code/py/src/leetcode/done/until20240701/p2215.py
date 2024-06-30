from rockyutil.leetcode import *


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_set, nums2_set = set(nums1), set(nums2)
        return [list(nums1_set - nums2_set), list(nums2_set - nums1_set)]
