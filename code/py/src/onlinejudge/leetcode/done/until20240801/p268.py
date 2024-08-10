from onlinejudge.leetcode import *


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, (i ^ num for i, num in enumerate(nums)), len(nums))
