from onlinejudge.leetcode import *


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ans = 1
        points.sort(key = lambda point: point[1])
        x = points[0][1]
        for start, end in points:
            if x < start:
                x = end
                ans += 1
        return ans
