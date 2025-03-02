from onlinejudge.leetcode import *


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        ans = 0
        for i in range(k - 1):
            colors.append(colors[i])
        prefs = [0]
        for lst, nxt in pairwise(colors):
            prefs.append(prefs[-1] + 1 if lst == nxt else prefs[-1])
        for i in range(len(colors) - k + 1):
            if 0 == prefs[i + k - 1] - prefs[i]:
                ans += 1
        return ans
