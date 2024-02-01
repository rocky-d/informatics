from rockyutil.leetcode import *


class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        a_points, b_points = 0, 0
        a_next = True
        for i, total_value in sorted(((i, a_value + b_value) for i, (a_value, b_value) in enumerate(zip(aliceValues, bobValues))), key = lambda item: item[1], reverse = True):
            if a_next:
                a_points += aliceValues[i]
            else:
                b_points += bobValues[i]
            a_next = not a_next
        return 1 if b_points < a_points else -1 if a_points < b_points else 0
