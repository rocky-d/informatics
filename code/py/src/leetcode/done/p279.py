class Solution:
    def numSquares(self, n: int) -> int:
        n1 = n + 1
        dp = [_i for _i in range(n1)]
        for perfect_square in [_i ** 2 for _i in range(int(n ** 0.5), 0, -1)]:
            for j in range(perfect_square, n1):
                dp[j] = min(dp[j], dp[j - perfect_square] + 1)
        return dp[-1]


sol = Solution()

eg_n = 13
print(sol.numSquares(eg_n))
