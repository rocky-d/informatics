from onlinejudge.leetcode import *


class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        seen = set()
        for char1, char2 in pairwise(s):
            seen.add(char1 + char2)
            if char2 + char1 in seen:
                ans = True
                break
        else:
            ans = False
        return ans
