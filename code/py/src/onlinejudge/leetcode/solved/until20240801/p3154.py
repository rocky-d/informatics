from onlinejudge.leetcode import *


class Solution:
    def waysToReachStair(self, k: int) -> int:
        @lru_cache(maxsize = None)
        def dfs(stair: int, down: bool, jump: int) -> int:
            if k < stair - 1:
                return 0
            res = 1 if k == stair else 0
            if down and 0 < stair:
                res += dfs(stair - 1, False, jump)
            res += dfs(stair + (0b1 << jump), True, jump + 1)
            return res

        return dfs(stair = 1, down = True, jump = 0)
