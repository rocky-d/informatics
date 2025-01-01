from onlinejudge.leetcode import *


class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        idx_1, idx_n = nums.index(1), nums.index(len(nums))
        return idx_1 - idx_n + len(nums) - (1 if idx_1 < idx_n else 2)
