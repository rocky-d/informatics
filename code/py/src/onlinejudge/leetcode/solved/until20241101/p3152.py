from onlinejudge.leetcode import *


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        prefs = list(accumulate((0 if 0b1 == lst ^ nxt else 1 for lst, nxt in pairwise(0b1 & num for num in nums)), initial=0))
        return [prefs[lo] == prefs[hi] for lo, hi in queries]
