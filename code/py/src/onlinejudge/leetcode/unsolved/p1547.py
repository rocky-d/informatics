from onlinejudge.leetcode import *


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        ans = 0
        sticks = []
        for lst, nxt in pairwise(chain([0], cuts, [n])):
            sticks.append(nxt - lst)
