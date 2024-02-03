from rockyutil.leetcode import *


class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        pres = [0]
        for stone in stones:
            pres.append(pres[-1] + stone)
        dp = [0 for _ in range(len(stones))]
        for i in range(2, 1 + len(stones)):
            dp_last, dp = dp, []
            for j in range(1 + len(stones) - i):
                dp.append(max(pres[j + i - 1] - pres[j] - dp_last[j],
                              pres[j + i] - pres[j + 1] - dp_last[j + 1]))
        return dp[0]


eg_stones = [5, 3, 1, 4, 2]
print(Solution().stoneGameVII(eg_stones))
