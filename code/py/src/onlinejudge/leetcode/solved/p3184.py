from onlinejudge.leetcode import *


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        return sum(1 for i, j in combinations(range(len(hours)), 2) if 0 == (hours[i] + hours[j]) % 24)
