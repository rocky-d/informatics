from rockyutil.leetcode import *


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if 3 > n:
            ans = 1 if 2 == n and nums[0] < nums[1] else 0
        else:
            max_, index = nums[0], 0
            for i in range(1, n - 1):
                max_, index = max(max_, nums[i]), i if nums[i] > max_ else index
                if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
                    ans = i
                    break
            else:
                ans = n - 1 if nums[-1] > max_ else index
        return ans
