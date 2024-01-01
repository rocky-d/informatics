from rockyutil.leetcode import *


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(), s.sort()
        i, j = 0, 0
        ans = 0
        while i < len(g) and j < len(s):
            if g[i] > s[j]:
                j += 1
            else:
                i += 1
                j += 1
                ans += 1
        return ans
