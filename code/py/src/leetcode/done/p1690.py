from rockyutil.leetcode import *


class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        pre = [0]
        for stone in stones:
            pre.append(pre[-1] + stone)
        dp = [0 for _ in range(1 + len(stones))]
        for i in range(1, 1 + len(stones)):
            dp_last, dp = dp, []
            for j in range(1 + len(stones) - i):
                dp.append(max(pre[j + i - 1] - pre[j] - dp_last[j],
                              pre[j + i] - pre[j + 1] - dp_last[j + 1]))
        return dp[0]


eg_stones = [5, 3, 1, 4, 2]
print(Solution().stoneGameVII(eg_stones))
