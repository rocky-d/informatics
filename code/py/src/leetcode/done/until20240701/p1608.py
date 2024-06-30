from rockyutil.leetcode import *


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        for x in range(1, 1 + len(nums)):
            if x == n - bisect_left(nums, x):
                ans = x
                break
        else:
            ans = -1
        return ans
