from rockyutil.leetcode import *


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        candies_max = max(candies)
        return [candies_max <= candy + extraCandies for candy in candies]
