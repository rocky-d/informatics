from onlinejudge.leetcode import *


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        ans = []
        items = sorted(((lft, i) for i, (lft, rit) in enumerate(intervals)), key = lambda item: item[0]) + [(1_000_001, -1)]
        for i, (lft, rit) in enumerate(intervals):
            ans.append(items[bisect_left(items, rit, key = lambda interval: interval[0])][1])
        return ans
