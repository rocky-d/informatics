from rockyutil.leetcode import *


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        ans = []
        dp = [[inf] * i + [j for j in range(n - i)] for i in range(n)]
        for u, v in queries:
            dp[u][v] = min(dp[u][v], 1)
            for a in range(0, u + 1):
                for b in range(v, n):
                    dp[a][b] = min(dp[a][b], dp[a][u] + dp[u][v] + dp[v][b])
            ans.append(dp[0][-1])
        return ans
