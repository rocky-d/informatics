from onlinejudge.leetcode import *


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        return all(0b1 & lst != 0b1 & nxt for lst, nxt in pairwise(nums))
