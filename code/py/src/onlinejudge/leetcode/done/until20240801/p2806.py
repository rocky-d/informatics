from onlinejudge.leetcode import *


class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        return 100 - 10 * (purchaseAmount // 10 if 0 <= purchaseAmount % 10 < 5 else purchaseAmount // 10 + 1)
