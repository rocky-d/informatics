from onlinejudge.leetcode import *


class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        @lru_cache(maxsize = None)
        def dfs(cnt0: int, cnt1: int, k: int) -> int:
            if 0 == cnt0 == cnt1:
                return 1
            res = 0
            if k < limit and 0 < cnt0:
                res += dfs(cnt0 - 1, cnt1, max(0, k) + 1)
            if -limit < k and 0 < cnt1:
                res += dfs(cnt0, cnt1 - 1, min(0, k) - 1)
            return res % 1_000_000_007

        ans = dfs(cnt0 = zero, cnt1 = one, k = 0)
        dfs.cache_clear()
        return ans


eg_zero = 3
eg_one = 3
eg_limit = 2
print(Solution().numberOfStableArrays(eg_zero, eg_one, eg_limit))
