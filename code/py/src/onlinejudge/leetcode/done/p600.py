from onlinejudge.leetcode import *


class Solution:
    def findIntegers(self, n: int) -> int:
        @lru_cache(maxsize = None)
        def dfs(i: int, limited: bool, one: bool) -> int:
            if 0 == i:
                return 1
            i -= 1
            up = n >> i & 0b1 if limited else 1
            res = dfs(i, limited and 0 == up, True)
            if 1 == up and one:
                res += dfs(i, limited, False)
            return res

        return dfs(i = n.bit_length(), limited = True, one = True)


eg_n = 2
print(Solution().findIntegers(eg_n))
