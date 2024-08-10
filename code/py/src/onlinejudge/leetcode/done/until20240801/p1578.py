from onlinejudge.leetcode import *


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        ans = 0
        left = 0
        while left + 1 < n:
            right = left + 1
            while right < n and colors[left] == colors[right]:
                right += 1
            ans += sum(neededTime[left:right]) - max(neededTime[left:right])
            left = right
        return ans


eg_colors = 'bbbaaa'
eg_neededTime = [4, 9, 3, 8, 8, 9]
print(Solution().minCost(colors = eg_colors, neededTime = eg_neededTime))
