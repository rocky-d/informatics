from onlinejudge.leetcode import *


class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        dp = [1] + [0] * target
        mod = 1_000_000_007
        for cnt, mark in types:
            total = cnt * mark
            if total < target:
                for vol in reversed(range(target + 1)):
                    for marks in range(mark, min(total, vol) + 1, mark):
                        dp[vol] += dp[vol - marks]
                        dp[vol] %= mod
            else:  # elif total >= target:
                for vol in range(mark, target + 1):
                    dp[vol] += dp[vol - mark]
                    dp[vol] %= mod
        return dp[-1]
