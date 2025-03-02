from onlinejudge.leetcode import *


class Solution:
    def check(self, nums: List[int]) -> bool:
        return sum(1 for lst, nxt in pairwise(chain(nums, [nums[0]])) if lst > nxt) <= 1
