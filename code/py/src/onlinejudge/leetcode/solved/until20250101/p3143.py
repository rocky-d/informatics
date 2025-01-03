from onlinejudge.leetcode import *


class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        ans = 0
        vis = set()
        for _, group in groupby(sorted((max(abs(x), abs(y)), c) for (x, y), c in zip(points, s)), key = lambda item: item[0]):
            cnt = 0
            for _, char in group:
                if char in vis:
                    break
                vis.add(char)
                cnt += 1
            else:
                ans += cnt
                continue
            break
        return ans
