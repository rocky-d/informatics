class Solution:
    def numTilings(self, n: int) -> int:
        dp = [(0, 1), (0, 1)]
        for i in range(2, 1 + n):
            dp.append((dp[-2][1] + dp[-1][0], dp[-2][1] + dp[-1][1] + 2 * dp[-1][0]))
        return dp[-1][1] % 1_000_000_007


eg_n = 3
print(Solution().numTilings(eg_n))
