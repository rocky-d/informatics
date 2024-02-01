from rockyutil.leetcode import *


class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        n = len(aliceValues)
        total_values = sorted(((i, a_value + b_value) for i, (a_value, b_value) in enumerate(zip(aliceValues, bobValues))), key = lambda item: item[1], reverse = True)
        a_points, b_points = sum(aliceValues[total_values[i][0]] for i in range(0, n, 2)), sum(bobValues[total_values[i][0]] for i in range(1, n, 2))
        return 1 if b_points < a_points else -1 if a_points < b_points else 0
