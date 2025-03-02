from onlinejudge.leetcode import *


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stk = deque()
        for char in s:
            if '(' == char:
                stk.append(char)
            else:  # elif ')' == char:
                if 0 < len(stk) and '(' == stk[-1]:
                    stk.pop()
                else:
                    stk.append(char)
        return len(stk)
