from onlinejudge.leetcode import *


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        for i, prices_i in enumerate(prices):
            for j in range(i + 1, n):
                if prices[j] <= prices_i:
                    prices[i] = prices_i - prices[j]
                    break
        return prices
