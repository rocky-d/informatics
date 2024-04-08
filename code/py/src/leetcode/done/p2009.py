from rockyutil.leetcode import *


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(frozenset(nums))
        interval = 0, 1
        idx, nums_len = 0, len(nums)
        while idx < nums_len:
            interval = max(interval, (idx, bisect_right(nums, nums[idx] + n - 1)), key = lambda item: item[1] - item[0])
            idx += 1
        return n - (interval[1] - interval[0])
