from onlinejudge.leetcode import *


class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        dp = [1] + [0] * target
        for cnt, mark in types:
            for vol in range(target, -1, -1):
                marks = 0
                for _ in range(cnt):
                    marks += mark
                    if vol < marks:
                        break
                    dp[vol] += dp[vol - marks]
                    dp[vol] %= 1_000_000_007
        return dp[-1]
