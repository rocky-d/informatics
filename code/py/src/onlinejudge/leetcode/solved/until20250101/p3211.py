from onlinejudge.leetcode import *


class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []
        stk = deque()

        def dfs(cnt: int, zero: bool) -> None:
            if 0 == cnt:
                ans.append(''.join(stk))
                return
            cnt -= 1
            if zero:
                stk.append('0')
                dfs(cnt, False)
                stk.pop()
            stk.append('1')
            dfs(cnt, True)
            stk.pop()

        dfs(cnt=n, zero=True)
        return ans
