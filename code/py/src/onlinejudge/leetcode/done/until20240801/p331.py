from collections import deque


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stk = deque()
        for val in preorder.split(','):
            stk.append(val)
            while 3 <= len(stk) and '#' == stk[-1] == stk[-2] and '#' != stk[-3]:
                stk.pop()
                stk.pop()
                stk.pop()
                stk.append('#')
        return 1 == len(stk) and '#' == stk[0]
