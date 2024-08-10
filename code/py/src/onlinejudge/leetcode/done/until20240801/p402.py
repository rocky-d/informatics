from onlinejudge.leetcode import *


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stk_inc = deque()
        for digit in map(int, num):
            while 0 < k and 0 < len(stk_inc) and digit < stk_inc[-1]:
                stk_inc.pop()
                k -= 1
            stk_inc.append(digit)
        for _ in range(k):
            stk_inc.pop()
        s = ''.join(map(str, stk_inc)).lstrip('0')
        return '0' if '' == s else s
