from onlinejudge.leetcode import *


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return reduce(lambda x, y: x + y, (list(combinations(nums, size)) for size in range(1 + len(nums))))
