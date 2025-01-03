from onlinejudge.leetcode import *


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(0, nxt - lst) for lst, nxt in pairwise(prices))
