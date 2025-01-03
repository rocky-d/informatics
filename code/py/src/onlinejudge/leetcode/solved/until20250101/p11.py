from onlinejudge.leetcode import *


class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        left = 0
        right = len(height) - 1
        while left < right:
            if height[left] < height[right]:
                ans = max(ans, (right - left) * height[left])
                left += 1
            else:
                ans = max(ans, (right - left) * height[right])
                right -= 1
        return ans
