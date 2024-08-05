from rockyutil.leetcode import *


class Solution:
    def findIntegers(self, n: int) -> int:
        if 1 == n:
            return 2
        ans = 2
        m = n.bit_length()
        dp = [1, 1]
        for _ in range(2, m):
            dp[0], dp[1] = max(dp[0], dp[1]), dp[0]
            ans += dp[1]
        s = bin(n)[2:]
        dp = [0, 1]
        tag = True
        for i, (lst, nxt) in enumerate(pairwise(s)):
            if '1' == lst == nxt:
                tag = False
            if tag:
                if '0' == nxt:
                    dp[0], dp[1] = max(dp[0], dp[1]), max(0, dp[0] - 1)
                else:
                    dp[0], dp[1] = max(dp[0], dp[1]), dp[0]
            else:
                dp[0], dp[1] = max(dp[0], dp[1]), dp[0]
        ans += dp[0] + dp[1]
        return ans


eg_n = 2
print(Solution().findIntegers(eg_n))
