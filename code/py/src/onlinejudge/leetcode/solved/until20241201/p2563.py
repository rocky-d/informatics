from onlinejudge.leetcode import *


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        cnt = 0
        nums.sort()
        for idx, num in enumerate(nums):
            idx1 = bisect_left(nums, lower - num)
            idx2 = bisect_right(nums, upper - num)
            cnt += idx2 - idx1 if not idx1 <= idx < idx2 else idx2 - idx1 - 1
        return cnt // 2
