from rockyutil.leetcode import *


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        len1, len2 = len(nums1), len(nums2)
        p1, p2 = 0, 0
        while p1 < len1 and p2 < len2:
            if nums1[p1] < nums2[p2]:
                p1 += 1
            elif nums2[p2] < nums1[p1]:
                p2 += 1
            else:
                ans = nums1[p1]
                break
        else:
            ans = -1
        return ans
