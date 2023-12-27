from rockyutil.leetcode import *


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        ans = 0
        i = 0
        while i + 1 < n:
            if colors[i] == colors[i + 1]:
                total_time, max_time = neededTime[i], neededTime[i]
                i += 1
                while i + 1 < n and colors[i] == colors[i + 1]:
                    total_time += neededTime[i]
                    max_time = max(max_time, neededTime[i])
                    i += 1
                ans += total_time + neededTime[i] - max(max_time, neededTime[i])
            i += 1
        return ans


eg_colors = 'bbbaaa'
eg_neededTime = [4, 9, 3, 8, 8, 9]
print(Solution().minCost(colors = eg_colors, neededTime = eg_neededTime))
