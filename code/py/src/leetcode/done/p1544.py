from rockyutil.leetcode import *


class Solution:
    def makeGood(self, s: str) -> str:
        stk = deque(['@'])
        oft = ord('a') - ord('A')
        for char in s:
            if oft == abs(ord(stk[-1]) - ord(char)):
                stk.pop()
            else:
                stk.append(char)
        stk.popleft()
        return ''.join(stk)
