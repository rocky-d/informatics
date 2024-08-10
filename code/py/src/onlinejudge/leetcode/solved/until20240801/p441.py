from onlinejudge.leetcode import *


class Solution:
    def arrangeCoins(self, n: int) -> int:
        return bisect_right(list(i * (i + 1) // 2 for i in range(ceil((n + n) ** 0.5))), n) - 1


eg_n = 7
print(Solution().arrangeCoins(n = eg_n))
