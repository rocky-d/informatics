from rockyutil.leetcode import *


class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        return max(bisect_right(tuple(sum(cost[k] * max(0, j * metals[k] - stock[k]) for k in range(n)) for j in range(1, 3000)), budget) for metals in composition)
