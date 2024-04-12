from rockyutil.leetcode import *


class Solution:
    def trap(self, height: List[int]) -> int:
        cnt = 0
        h1, h2 = 0, 0
        for i, j in zip(range(len(height)), reversed(range(len(height)))):
            h1, h2 = max(h1, height[i]), max(h2, height[j])
            cnt += h1 + h2 - height[i]
        return cnt - h1 * len(height)
