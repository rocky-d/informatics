from onlinejudge.leetcode import *


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(frozenset(nums1) & frozenset(nums2))
