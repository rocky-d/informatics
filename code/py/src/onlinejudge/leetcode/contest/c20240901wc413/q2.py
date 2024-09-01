from onlinejudge.leetcode import *


class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        ans = []
        sl = sc.SortedList([0])
        for i, (x, y) in enumerate(queries, start=1):
            sl.add(abs(x) + abs(y))
            ans.append(-1 if i < k else sl[k])
        return ans
