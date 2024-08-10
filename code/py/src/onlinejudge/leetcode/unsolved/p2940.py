from library.datastructure.segmenttree import SegmentTree
from onlinejudge.leetcode import *


class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        n = len(heights)
        idxes = range(n)
        root = SegmentTree(max, heights)
        for a, b in queries:
            if a > b:
                a, b = b, a
            if a == b or heights[a] < heights[b]:
                ans.append(b)
                continue
            b += 1
            res = bisect_right(idxes, heights[a], lo = b, key = lambda mid: root.query(b, mid + 1))
            ans.append(res if res < n else -1)
        return ans
