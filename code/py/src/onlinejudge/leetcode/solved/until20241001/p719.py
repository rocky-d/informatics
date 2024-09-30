from onlinejudge.leetcode import *


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        return bisect_left(range(nums[-1] - nums[0] + 1), k, key = lambda mid: sum(i - bisect_left(nums, num - mid, hi = i) for i, num in enumerate(nums)))
