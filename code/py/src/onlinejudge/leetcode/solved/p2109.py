from onlinejudge.leetcode import *


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ls = list()
        i, n = 0, len(spaces)
        for idx, char in enumerate(s):
            if i < n and idx == spaces[i]:
                i += 1
                ls.append(' ')
            ls.append(char)
        return ''.join(ls)
