from onlinejudge.leetcode import *


class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        for _ in range(len(customers)):
            if 0 == customers[-1]:
                customers.pop(-1)
            else:
                break
        rotations = 0
        profit = 0
        waiting = 0
        for customer in customers:
            waiting += customer
            boarding = min(4, waiting)
            waiting -= boarding
            profit += boarding * boardingCost - runningCost
            rotations += 1
        while 4 <= waiting:
            boarding = waiting if waiting < 4 else 4
            waiting -= boarding
            profit += boarding * boardingCost - runningCost
            rotations += 1
        if runningCost < waiting * boardingCost:
            profit += waiting * boardingCost - runningCost
            rotations += 1
        return rotations if 0 < profit else -1
