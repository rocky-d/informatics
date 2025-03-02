from onlinejudge.leetcode import *


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        return sum(1 for x, y in combinations(hours, 2) if 0 == (x + y) % 24)
