from onlinejudge.leetcode import *


class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        dp = [0, 0, 0]
        for a, b in zip(energyDrinkA, energyDrinkB):
            dp[0], dp[1], dp[2] = max(dp[1], dp[2]), max(dp[0], dp[1]) + a, max(dp[0], dp[2]) + b
        return max(dp[1], dp[2])
