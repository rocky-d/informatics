from onlinejudge.leetcode import *


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        return all(0b1 == lst ^ nxt for lst, nxt in pairwise(0b1 & num for num in nums))
