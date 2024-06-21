from rockyutil.leetcode import *


class Solution:
    def temperatureTrend(self, temperatureA: List[int], temperatureB: List[int]) -> int:
        ans, cnt = 0, 0
        for a, b in zip((+1 if lst < nxt else 0 if lst == nxt else -1 for lst, nxt in pairwise(temperatureA)), (+1 if lst < nxt else 0 if lst == nxt else -1 for lst, nxt in pairwise(temperatureB))):
            if a == b:
                cnt += 1
            else:
                ans = max(ans, cnt)
                cnt = 0
        ans = max(ans, cnt)
        return ans
