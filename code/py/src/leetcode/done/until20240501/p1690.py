from rockyutil.leetcode import *


class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        dp = [0 for _ in range(n)]
        pre, p = 0, 0
        for i in range(2, 1 + n):
            dp_last, dp = dp, []
            pre += stones[p]
            p += 1
            pre2 = pre
            for j in range(0, 1 + n - i):
                pre1, pre2 = pre2, pre2 - stones[j] + stones[j + i - 1]
                dp.append(max(pre1 - dp_last[j], pre2 - dp_last[j + 1]))
        return dp[0]


eg_stones = [7, 90, 5, 1, 100, 10, 10, 2]
print(Solution().stoneGameVII(eg_stones))
