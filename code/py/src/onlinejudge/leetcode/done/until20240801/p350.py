from onlinejudge.leetcode import *


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnter1, cnter2 = Counter(nums1), Counter(nums2)
        return reduce(add, ([num] * min(cnter1[num], cnter2[num]) for num in cnter1.keys() & cnter2.keys()), [])
