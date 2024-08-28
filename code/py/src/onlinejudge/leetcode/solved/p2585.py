from onlinejudge.leetcode import *


class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        dp = [[0, 1]] + [[0, 0] for _ in range(target)]
        for count, mark in types:
            for vol in range(target, -1, -1):
                marks = 0
                for _ in range(count):
                    marks += mark
                    if vol < marks:
                        break
                    if dp[vol][0] < dp[vol - marks][0] + marks:
                        dp[vol][0], dp[vol][1] = dp[vol - marks][0] + marks, dp[vol - marks][1]
                    elif dp[vol][0] == dp[vol - marks][0] + marks:
                        dp[vol][1] += dp[vol - marks][1]
                        dp[vol][1] %= 1_000_000_007
        return dp[-1][1]