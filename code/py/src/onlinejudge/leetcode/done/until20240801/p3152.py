from onlinejudge.leetcode import *


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        prefs = [0]
        for lst, nxt in pairwise(nums):
            prefs.append(prefs[-1] + 1 if 0b1 & lst == 0b1 & nxt else prefs[-1])
        return [prefs[fr] == prefs[to] for fr, to in queries]
