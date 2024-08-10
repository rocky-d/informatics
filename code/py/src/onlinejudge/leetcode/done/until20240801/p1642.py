from onlinejudge.leetcode import *


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap_min = []
        for i, (lst, nxt) in enumerate(pairwise(heights)):
            diff = nxt - lst
            if 0 < diff:
                heappush(heap_min, diff)
                if ladders < len(heap_min):
                    bricks -= heappop(heap_min)
                    if bricks < 0:
                        ans = i
                        break
        else:
            ans = len(heights) - 1
        return ans
