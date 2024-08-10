from rockyutil.datastructure.segmenttree import SegmentTree
from rockyutil.leetcode import *


class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        n = len(heights)
        root = SegmentTree(max, heights)
        for a, b in queries:
            if a > b:
                a, b = b, a
            if a == b or heights[a] < heights[b]:
                ans.append(b)
                continue
            b += 1
            res = b + bisect_right(range(b, n), heights[a], key = lambda mid: root.query(b, mid + 1))
            ans.append(res if res < n else -1)
        return ans
