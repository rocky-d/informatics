from onlinejudge.leetcode import *


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        return max(sum(0b1 & candidate >> i for candidate in candidates) for i in range(24))
