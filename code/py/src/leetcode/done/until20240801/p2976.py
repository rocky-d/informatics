from rockyutil.leetcode import *


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        range_26 = range(26)
        dp = [[inf] * 26 for _ in range_26]
        for u, v, w in zip(original, changed, cost):
            u, v = ord(u) - ord('a'), ord(v) - ord('a')
            dp[u][v] = min(dp[u][v], w)
        for k in range_26:
            for u in range_26:
                for v in range_26:
                    dp[u][v] = min(dp[u][v], dp[u][k] + dp[k][v])
        ans = sum(0 if si == ti else dp[ord(si) - ord('a')][ord(ti) - ord('a')] for si, ti in zip(source, target))
        if isinf(ans):
            ans = -1
        return ans
