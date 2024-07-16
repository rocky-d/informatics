from rockyutil.leetcode import *


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1, set2 = frozenset(nums1), frozenset(nums2)
        return [sum(1 for num in nums1 if num in set2), sum(1 for num in nums2 if num in set1)]
