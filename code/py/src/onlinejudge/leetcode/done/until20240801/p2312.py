from onlinejudge.leetcode import *


class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        prices_dict = {(x, y): price for x, y, price in prices}
        dp = [[0 for _ in range(1 + n)] for _ in range(1 + m)]
        for i in range(1, 1 + m):
            for j in range(1, 1 + n):
                dp[i][j] = max(
                    prices_dict.get((i, j), 0),
                    max((dp[x][j] + dp[i - x][j] for x in range(1, i)), default = 0),
                    max((dp[i][y] + dp[i][j - y] for y in range(1, j)), default = 0),
                )
        return dp[-1][-1]
