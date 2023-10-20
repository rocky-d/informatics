from leetcode.leetcode import *


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        amount1 = amount + 1
        dp = [1] + [0 for _i in range(amount)]
        for coin in coins:
            for j in range(coin, amount1):
                dp[j] += dp[j - coin]
        return dp[-1]


sol = Solution()

eg_amount = 5
eg_coins = [1, 2, 5]
print(sol.change(amount = eg_amount, coins = eg_coins))
