from onlinejudge.leetcode import *


class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        vis = set()
        for lst, nxt in pairwise(s):
            vis.add(lst + nxt)
            if nxt + lst in vis:
                ans = True
                break
        else:
            ans = False
        return ans
