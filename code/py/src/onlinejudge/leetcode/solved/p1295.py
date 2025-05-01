from onlinejudge.leetcode import *


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(1 for num in nums if 0b0 == 0b1 & len(str(num)))
