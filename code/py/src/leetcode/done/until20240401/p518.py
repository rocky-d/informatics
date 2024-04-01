from rockyutil.leetcode import *


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0 for _ in range(amount)]
        for coin in coins:
            for vol in range(coin, amount + 1):
                dp[vol] += dp[vol - coin]
        return dp[-1]


eg_amount = 5
eg_coins = [1, 2, 5]
print(Solution().change(eg_amount, eg_coins))
