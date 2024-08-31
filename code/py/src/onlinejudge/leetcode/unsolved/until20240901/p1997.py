from onlinejudge.leetcode import *


class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        dp = [0 for _ in nextVisit]
        dp[0] = 2
        for i in range(1, len(nextVisit)):
            nxt = nextVisit[i]
            dp[i] = dp[i - 1] + dp[i - 1] + 2
            if 0 < nxt:
                dp[i] -= dp[nxt - 1]
            dp[i] %= 1_000_000_007
        return dp[-2]
