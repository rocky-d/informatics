from onlinejudge.leetcode import *


class Solution:
    def finalString(self, s: str) -> str:
        ans = deque()
        reverse = False
        for char in s:
            if 'i' == char:
                reverse = not reverse
            else:
                if reverse:
                    ans.appendleft(char)
                else:
                    ans.append(char)
        return ''.join(reversed(ans) if reverse else ans)
