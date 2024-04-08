from rockyutil.leetcode import *


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        n_1 = n - 1
        nums = sorted(frozenset(nums))
        interval = 0, 0
        lo, nums_len = 0, len(nums)
        for i, num in enumerate(nums):
            lo = bisect_right(nums, num + n_1, lo = lo)
            interval = max(interval, (i, lo), key = lambda item: item[1] - item[0])
            if lo == nums_len:
                break
        return n - (interval[1] - interval[0])
