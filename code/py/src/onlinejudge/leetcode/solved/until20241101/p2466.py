from onlinejudge.leetcode import *


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = defaultdict(lambda: 0)
        dp[0] += 1
        for i in range(min(zero, one), high + 1):
            dp[i] += dp[i - zero]
            dp[i] += dp[i - one]
        return sum(cnt for leng, cnt in dp.items() if low <= leng) % 1_000_000_007
