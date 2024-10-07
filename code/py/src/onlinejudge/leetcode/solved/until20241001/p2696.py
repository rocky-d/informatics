from onlinejudge.leetcode import *


class Solution:
    def minLength(self, s: str) -> int:
        ans = len(s)
        stk = deque()
        for char in s:
            if 'A' == char or 'C' == char:
                stk.append(char)
                continue
            elif 'B' == char:
                if 0 < len(stk) and 'A' == stk[-1]:
                    stk.pop()
                    ans -= 2
                    continue
            elif 'D' == char:
                if 0 < len(stk) and 'C' == stk[-1]:
                    stk.pop()
                    ans -= 2
                    continue
            stk.clear()
        return ans


eg_s = 'ABFCACDB'
print(Solution().minLength(eg_s))
