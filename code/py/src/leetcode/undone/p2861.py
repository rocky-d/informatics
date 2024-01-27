from rockyutil.leetcode import *


class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        return max(bisect_right(range(1, 1_000_000_000), budget, key = lambda count: sum(cost[j] * max(0, count * composition[i][j] - stock[j]) for j in range(n))) for i in range(k))
