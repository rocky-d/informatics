from rockyutil.leetcode import *


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return [sum(1 for num in nums1 if num in nums2), sum(1 for num in nums2 if num in nums1)]
