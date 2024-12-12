from onlinejudge.leetcode import *


class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        return sum(value * day for day, value in enumerate(sorted(chain(*values)), start=1))
