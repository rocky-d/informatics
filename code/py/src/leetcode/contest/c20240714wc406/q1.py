from rockyutil.leetcode import *


class Solution:
    def getSmallestString(self, s: str) -> str:
        ls = list(s)
        for i, (lst, nxt) in enumerate(pairwise(s)):
            if 0b1 & int(lst) == 0b1 & int(nxt) and int(lst) > int(nxt):
                ls[i], ls[i + 1] = s[i + 1], s[i]
                break
        return ''.join(ls)
