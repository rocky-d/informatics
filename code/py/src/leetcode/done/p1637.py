from rockyutil.leetcode import *


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_points = sorted([point[0] for point in points])
        ans = 0
        for i in range(1, len(x_points)):
            ans = max(ans, x_points[i] - x_points[i - 1])
        return ans
