from onlinejudge.leetcode import *


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [1]
        for row in range(1, 1 + rowIndex):
            dp_lst, dp = dp, [...] + [...] * row
            dp[0] = dp_lst[0]
            for i, (lst, nxt) in enumerate(pairwise(dp_lst), start=1):
                dp[i] = lst + nxt
            dp[-1] = dp_lst[-1]
        return dp
