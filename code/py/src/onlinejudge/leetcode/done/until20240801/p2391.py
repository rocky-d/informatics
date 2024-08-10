from onlinejudge.leetcode import *


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        cnt = 0
        m, p, g = 0, 0, 0
        for i, s in enumerate(garbage):
            cnt += len(s)
            for char in s:
                if 'M' == char:
                    m = i
                elif 'P' == char:
                    p = i
                else:  # elif 'G' == char:
                    g = i
        travel = list(accumulate(travel, initial = 0))
        return cnt + travel[m] + travel[p] + travel[g]
