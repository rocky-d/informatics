from onlinejudge.leetcode import *


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(xor, nums)
