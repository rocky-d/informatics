from rockyutil.leetcode import *


class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        ans = 0
        water = 0
        for i, plant in enumerate(plants):
            if water < plant:
                water = capacity
                ans += 2 * i
            water -= plant
            ans += 1
        return ans
