from onlinejudge.leetcode import *


class Solution:
    def removeStars(self, s: str) -> str:
        stk = deque(maxlen = len(s))
        for char in s:
            if '*' == char:
                stk.pop()
            else:
                stk.append(char)
        return ''.join(stk)


eg_s = 'leet**cod*e'
print(Solution().removeStars(eg_s))
