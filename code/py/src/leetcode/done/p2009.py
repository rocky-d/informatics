from rockyutil.leetcode import *


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(frozenset(nums))
        interval = 0, 0
        for i in range(len(nums)):
            interval = max(interval, (i, bisect_right(nums, nums[i] + n - 1)), key = lambda item: item[1] - item[0])
        return n - (interval[1] - interval[0])
