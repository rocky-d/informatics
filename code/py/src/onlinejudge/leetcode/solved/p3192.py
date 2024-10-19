from onlinejudge.leetcode import *


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        return sum(1 for _ in groupby(nums)) - nums[0]
