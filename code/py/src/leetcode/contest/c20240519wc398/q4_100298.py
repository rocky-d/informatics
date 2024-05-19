from rockyutil.leetcode import *


class Solution:
    def waysToReachStair(self, k: int) -> int:
        @cache
        def dfs(stair: int, jump: int, down: bool) -> int:
            if k < stair - 1:
                return 0
            res = 0
            if k == stair:
                res += 1
            if down and 0 < stair:
                res += dfs(stair - 1, jump, False)
            res += dfs(stair + (0b1 << jump), jump + 1, True)
            return res

        return dfs(stair = 1, jump = 0, down = True)


eg_k = 1
print(Solution().waysToReachStair(eg_k))
