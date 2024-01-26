class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for _ in range(maxMove):
            dp_last = dp
            dp = []
            for j in range(m):
                dp.append([])
                for k in range(n):
                    dp[-1].append(0)
                    dp[-1][-1] += 1 if j == 0 else dp_last[j - 1][k]
                    dp[-1][-1] += 1 if j == m - 1 else dp_last[j + 1][k]
                    dp[-1][-1] += 1 if k == 0 else dp_last[j][k - 1]
                    dp[-1][-1] += 1 if k == n - 1 else dp_last[j][k + 1]
        return dp[startRow][startColumn] % 1_000_000_007


eg_m = 1
eg_n = 3
eg_maxMove = 3
eg_startRow = 0
eg_startColumn = 1
print(Solution().findPaths(m = eg_m, n = eg_n, maxMove = eg_maxMove, startRow = eg_startRow, startColumn = eg_startColumn))
