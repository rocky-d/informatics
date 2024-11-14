from onlinejudge.leetcode import *


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        lo, hi = 0, sum(quantities) + 1
        while 1 < hi - lo:
            mid = lo + hi >> 1
            if n < sum(ceil(quantity / mid) for quantity in quantities):
                lo = mid
            else:
                hi = mid
        return hi
