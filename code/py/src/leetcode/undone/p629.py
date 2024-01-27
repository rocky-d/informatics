class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [[1] + [0 for _ in range(k)] for _ in range(n)]
        for i in range(1, n):
            for j in range(1, 1 + k):
                dp[i][j] = sum(dp[i - 1][max(0, j - i):j + 1])
        return dp[-1][-1] % 1_000_000_007


eg_n = 3
eg_k = 1
print(Solution().kInversePairs(n = eg_n, k = eg_k))
