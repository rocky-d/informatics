from onlinejudge.leetcode import *


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        dp = points.pop(0)
        for row in points:
            dp_lst, dp = dp, [0] * n
            maxm = -inf
            for i in range(n):
                maxm = max(maxm, dp_lst[i] + i)
                dp[i] = max(dp[i], maxm + row[i] - i)
            maxm = -inf
            for i in reversed(range(n)):
                maxm = max(maxm, dp_lst[i] - i)
                dp[i] = max(dp[i], maxm + row[i] + i)
        return max(dp)


points = [
    [1, 5],
    [2, 3],
    [4, 2],
]
print(Solution().maxPoints(points))
