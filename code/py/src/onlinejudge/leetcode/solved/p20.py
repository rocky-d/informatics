from onlinejudge.leetcode import *


class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', ']': '[', '}': '{'}
        stk = deque()
        for char in s:
            if char in '([{':
                stk.append(char)
            elif 0 < len(stk) and stk[-1] == pairs[char]:
                stk.pop()
            else:
                ans = False
                break
        else:
            ans = 0 == len(stk)
        return ans
