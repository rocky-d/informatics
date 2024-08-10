from onlinejudge.leetcode import *


class Solution:
    def reverseParentheses(self, s: str) -> str:
        ans = ''
        stk = deque()
        for char in s:
            if '(' == char:
                stk.append(ans)
                ans = ''
            elif ')' == char:
                ans = stk.pop() + ans[::-1]
            else:
                ans += char
        return ans
