from onlinejudge.leetcode import *


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ans = []
        i1, n1 = 0, len(nums1)
        i2, n2 = 0, len(nums2)
        while i1 < n1 or i2 < n2:
            if 0 < len(ans):
                while True:
                    if i1 < n1 and ans[-1][0] == nums1[i1][0]:
                        ans[-1][1] += nums1[i1][1]
                        i1 += 1
                    elif i2 < n2 and ans[-1][0] == nums2[i2][0]:
                        ans[-1][1] += nums2[i2][1]
                        i2 += 1
                    else:
                        break
            if i1 < n1 and i2 < n2:
                if nums1[i1][0] < nums2[i2][0]:
                    ans.append([nums1[i1][0], nums1[i1][1]])
                    i1 += 1
                elif nums1[i1][0] > nums2[i2][0]:
                    ans.append([nums2[i2][0], nums2[i2][1]])
                    i2 += 1
                else:  # elif nums1[i1][0] == nums2[i2][0]:
                    ans.append([nums1[i1][0], nums1[i1][1] + nums2[i2][1]])
                    i1 += 1
                    i2 += 1
            else:  # elif not (i1 < n1 and i2 < n2):
                while i1 < n1:
                    ans.append([nums1[i1][0], nums1[i1][1]])
                    i1 += 1
                while i2 < n2:
                    ans.append([nums2[i2][0], nums2[i2][1]])
                    i2 += 1
        return ans
