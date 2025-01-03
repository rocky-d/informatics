from onlinejudge.leetcode import *


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        return bisect_left(range(max(quantities) + 1), -n, lo=1, key=lambda mid: -sum(ceil(quantity / mid) for quantity in quantities))
