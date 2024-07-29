from rockyutil.leetcode import *


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 0, 1_000_000_001
        while 1 < hi - lo:
            mid = lo + hi >> 1
            if h < sum(ceil(pile / mid) for pile in piles):
                lo = mid
            else:
                hi = mid
        return hi
