from onlinejudge.leetcode import *


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        eve, odd = 0, 1
        while eve < n and odd < n:
            if 0b0 == 0b1 & nums[eve]:
                eve += 2
            elif 0b1 == 0b1 & nums[odd]:
                odd += 2
            else:
                nums[eve], nums[odd] = nums[odd], nums[eve]
                eve += 2
                odd += 2
        return nums
