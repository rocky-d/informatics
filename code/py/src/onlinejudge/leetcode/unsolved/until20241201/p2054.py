from onlinejudge.leetcode import *


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        ls = [(0, 0)]
        for start, end, value in sorted(events, key=lambda item: (item[1], item[0], item[2])):
            ls.append((end, ls[bisect_right(ls, start - 1, key=lambda item: item[0]) - 1][1] + value))
        return max(score for _, score in ls)


eg_events = [
    [10, 83, 53],
    [63, 87, 45],
    [97, 100, 32],
    [51, 61, 16],
]
print(Solution().maxTwoEvents(eg_events))
