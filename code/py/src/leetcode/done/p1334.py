from rockyutil.leetcode import *


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        range_n = range(n)
        dp = [[inf] * n for _ in range_n]
        for u, v, w in edges:
            dp[u][v] = dp[v][u] = w
        for k in range_n:
            for u in range_n:
                for v in range_n:
                    dp[u][v] = min(dp[u][v], dp[u][k] + dp[k][v])
        return max((sum(-1 for v in chain(range(u), range(u + 1, n)) if dp[u][v] <= distanceThreshold), u) for u in range_n)[1]
