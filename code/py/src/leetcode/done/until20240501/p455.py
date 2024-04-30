from rockyutil.leetcode import *


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(), s.sort()
        i, j = 0, 0
        ans = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                ans += 1
                i += 1
            j += 1
        return ans
