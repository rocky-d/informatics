from onlinejudge.leetcode import *


class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        dp = [1] + [0] * target
        for cnt, mark in types:
            if cnt * mark < target:
                total = cnt * mark
                for vol in reversed(range(target + 1)):
                    for marks in range(mark, min(total, vol) + 1, mark):
                        dp[vol] += dp[vol - marks]
                        dp[vol] %= 1_000_000_007
            else:  # elif cnt * mark >= target:
                for vol in range(mark, target + 1):
                    dp[vol] += dp[vol - mark]
                    dp[vol] %= 1_000_000_007
        return dp[-1]
