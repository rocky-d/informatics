from rockyutil.leetcode import *


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        minm = nums[0]
        for num in nums:
            if num < minm:
                ans += minm - num
                minm += 1
            else:
                minm = num + 1
        return ans
