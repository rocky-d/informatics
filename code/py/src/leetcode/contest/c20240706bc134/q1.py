from rockyutil.leetcode import *


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        ans = 0
        for i in range(1, len(colors) - 1):
            if colors[i - 1] != colors[i] and colors[i] != colors[i + 1]:
                ans += 1
        if colors[-1] != colors[0] and colors[0] != colors[1]:
            ans += 1
        if colors[-2] != colors[-1] and colors[-1] != colors[0]:
            ans += 1
        return ans
