from onlinejudge.leetcode import *


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        money_left = money - sum(sorted(prices)[:2])
        return money_left if 0 <= money_left else money
