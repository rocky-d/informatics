from onlinejudge.leetcode import *


class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        return all(lst != nxt for lst, nxt in pairwise(grid[0])) and all(lst == nxt for lst, nxt in pairwise(grid))
