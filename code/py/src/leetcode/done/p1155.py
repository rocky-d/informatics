class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [1] + [0 for _ in range(target)]
        for i in range(n):
            for j in range(target, -1, -1):
                dp[j] = 0
                for k_ in range(min(k, j), 0, -1):
                    dp[j] += dp[j - k_]
        return dp[-1] % (10 ** 9 + 7)


eg_n = 2
eg_k = 6
eg_target = 7
print(Solution().numRollsToTarget(n = eg_n, k = eg_k, target = eg_target))
