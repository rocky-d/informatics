from onlinejudge.leetcode import *


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ans = 0
        cnter = [0] * (1 + max(heights))
        for height in heights:
            cnter[height] += 1
        idx = 0
        for height, cnt in enumerate(cnter):
            for _ in range(cnt):
                if height != heights[idx]:
                    ans += 1
                idx += 1
        return ans
