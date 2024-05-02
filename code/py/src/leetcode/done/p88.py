from rockyutil.leetcode import *


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p = m + n - 1
        p1, p2 = m - 1, n - 1
        while 0 <= p1 and 0 <= p2:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
                p -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
                p -= 1
        if -1 == p1:
            nums1[:p + 1] = nums2[:p2 + 1]
        else:  # elif -1 == p2:
            nums1[:p + 1] = nums1[:p1 + 1]
