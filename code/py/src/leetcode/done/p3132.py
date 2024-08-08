from rockyutil.leetcode import *


class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        ans = inf
        nums1.sort()
        nums2.sort()
        for i, j in combinations(range(len(nums1)), r = 2):
            nums3 = nums1[:i] + nums1[i + 1:j] + nums1[j + 1:]
            diff = nums2[0] - nums3[0]
            if all(diff == x - y for x, y in zip(nums2, nums3)):
                ans = min(ans, diff)
        return ans
