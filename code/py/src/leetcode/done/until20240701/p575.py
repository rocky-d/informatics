from rockyutil.leetcode import *


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(candyType) // 2, len(frozenset(candyType)))
