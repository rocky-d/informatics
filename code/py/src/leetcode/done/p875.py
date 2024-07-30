from rockyutil.leetcode import *


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        return bisect_left(range(1_000_000_001), -h, lo = 1, key = lambda x: -sum(ceil(pile / x) for pile in piles))
