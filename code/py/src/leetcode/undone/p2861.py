from rockyutil.leetcode import *


class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        return max(bisect_right(range(1, 200_000_001), budget, key = lambda count: sum(cost_ * max(0, count * metal_ - stock_) for metal_, stock_, cost_ in zip(metal, stock, cost))) for metal in composition)
