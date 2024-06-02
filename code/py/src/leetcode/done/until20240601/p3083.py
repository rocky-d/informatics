from rockyutil.leetcode import *


class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        seen = set()
        for lst, nxt in pairwise(s):
            seen.add(lst + nxt)
            if nxt + lst in seen:
                ans = True
                break
        else:
            ans = False
        return ans
