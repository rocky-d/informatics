from onlinejudge.leetcode import *


class Solution:
    def clearDigits(self, s: str) -> str:
        stk = deque()
        for char in s:
            if char.isnumeric() and 0 < len(stk) and not stk[-1].isnumeric():
                stk.pop()
            else:
                stk.append(char)
        return ''.join(stk)
