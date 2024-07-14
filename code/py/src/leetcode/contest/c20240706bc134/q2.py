from rockyutil.leetcode import *


class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        ans = 0
        enemyEnergies.sort()
        if currentEnergy < enemyEnergies[0]:
            return ans
        while 0 < len(enemyEnergies):
            if enemyEnergies[0] <= currentEnergy:
                currentEnergy -= enemyEnergies[0]
                ans += 1
            else:
                currentEnergy += enemyEnergies.pop(-1)
        return ans
