from onlinejudge.leetcode import *


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        lfts, rits = deque(), deque()
        stk_incs = deque()
        for i, height in zip(range(n), heights):
            while 0 < len(stk_incs) and height <= heights[stk_incs[-1]]:
                stk_incs.pop()
            lfts.append(-1 if 0 == len(stk_incs) else stk_incs[-1])
            stk_incs.append(i)
        stk_incs.clear()
        for i, height in zip(reversed(range(n)), reversed(heights)):
            while 0 < len(stk_incs) and height <= heights[stk_incs[-1]]:
                stk_incs.pop()
            rits.appendleft(n if 0 == len(stk_incs) else stk_incs[-1])
            stk_incs.append(i)
        return max(height * (rit - lft - 1) for height, lft, rit in zip(heights, lfts, rits))
