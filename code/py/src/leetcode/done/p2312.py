from rockyutil.leetcode import *


class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        prices_dict = {(x, y): price for x, y, price in prices}

        @cache
        def dfs(a: int, b: int) -> int:
            res = prices_dict.get((a, b), 0)
            for x in range(1, a):
                res = max(res, dfs(x, b) + dfs(a - x, b))
            for y in range(1, b):
                res = max(res, dfs(a, y) + dfs(a, b - y))
            return res

        return dfs(a = m, b = n)
