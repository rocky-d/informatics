from onlinejudge.leetcode import *


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        new_lft, new_rit = newInterval
        idx, n = 0, len(intervals)
        while idx < n and intervals[idx][1] < new_lft:
            ans.append(intervals[idx])
            idx += 1
        if idx < n:
            new_lft = min(new_lft, intervals[idx][0])
        while idx < n and intervals[idx][0] <= new_rit:
            idx += 1
        if 0 <= idx - 1 < n:
            new_rit = max(new_rit, intervals[idx - 1][1])
        ans.append([new_lft, new_rit])
        while idx < n:
            ans.append(intervals[idx])
            idx += 1
        return ans


eg_intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
eg_newInterval = [4, 8]
print(Solution().insert(eg_intervals, eg_newInterval))
