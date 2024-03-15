from rockyutil.leetcode import *


class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        prices_dict = {(x, y): price for x, y, price in prices}

        @cache
        def dfs(a: int, b: int) -> int:
            return max(
                prices_dict.get((a, b), 0),
                max((dfs(x, b) + dfs(a - x, b) for x in range(1, a)), default = 0),
                max((dfs(a, y) + dfs(a, b - y) for y in range(1, b)), default = 0),
            )

        return dfs(a = m, b = n)
