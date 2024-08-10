from onlinejudge.leetcode import *


class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        return reduce(add, ([nums[i + 1], nums[i]] for i in range(0, len(nums), 2)))
