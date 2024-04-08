from rockyutil.leetcode import *


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        n_1 = n - 1
        nums = sorted(frozenset(nums))
        interval = 0, 0
        for i in range(len(nums)):
            interval = max(interval, (i, bisect_right(nums, nums[i] + n_1)), key = lambda item: item[1] - item[0])
        return n - (interval[1] - interval[0])
