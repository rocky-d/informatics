from rockyutil.leetcode import *


class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        pre = [0]
        for stone in stones:
            pre.append(pre[-1] + stone)

        @cache
        def dfs(a, b):
            if a == b:
                return 0
            return max(pre[b - 1] - pre[a] - dfs(a = a, b = b - 1),
                       pre[b] - pre[a + 1] - dfs(a = a + 1, b = b))

        ans = dfs(a = 0, b = len(stones))
        dfs.cache_clear()
        return ans
