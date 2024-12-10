class Solution:
    def knightDialer(self, n: int) -> int:
        nxts = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]
        dp = [1] * 10
        for _ in range(1, n):
            dp_lst, dp = dp, [0] * 10
            for lst in range(10):
                for nxt in nxts[lst]:
                    dp[nxt] += dp_lst[lst]
                    dp[nxt] %= 1_000_000_007
        return sum(dp) % 1_000_000_007
