from onlinejudge.leetcode import *


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: (interval[1], interval[0]))
        dp = [(-inf, 0)]
        for lo, hi in intervals:
            insort(dp, (hi, max(dp[-1][1], dp[bisect_right(dp, (lo, inf)) - 1][1] + 1)))
        return len(intervals) - dp[-1][1]


eg_intervals = [[1, 2], [2, 3]]
print(Solution().eraseOverlapIntervals(eg_intervals))
