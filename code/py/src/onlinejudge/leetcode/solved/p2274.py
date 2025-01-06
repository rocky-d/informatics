from onlinejudge.leetcode import *


class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        return max(nxt - lst - 1 for lst, nxt in pairwise(chain([bottom - 1], sorted(special), [top + 1])))
