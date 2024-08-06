from rockyutil.leetcode import *


class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        cover = 0b1 << limit

        @lru_cache(maxsize = None)
        def dfs(cnt0: int, cnt1: int, diff: int, bits: int) -> int:
            if 0 == cnt0 == cnt1:
                return 1
            res = 0
            if -limit < diff and 0 < cnt0:
                if limit < bits.bit_length():
                    res += dfs(cnt0 - 1, cnt1, diff - (-1 if 0b0 == 0b1 & (bits >> limit - 1) else +1) - 1,
                               cover | ((bits << 1) | 0b0))
                else:
                    res += dfs(cnt0 - 1, cnt1, diff - 1, (bits << 1) | 0b0)
            if diff < limit and 0 < cnt1:
                if limit < bits.bit_length():
                    res += dfs(cnt0, cnt1 - 1, diff - (-1 if 0b0 == 0b1 & (bits >> limit - 1) else +1) + 1,
                               cover | ((bits << 1) | 0b1))
                else:
                    res += dfs(cnt0, cnt1 - 1, diff + 1, (bits << 1) | 0b1)
            return res

        return dfs(cnt0 = zero, cnt1 = one, diff = 0, bits = 0b1)


eg_zero = 3
eg_one = 3
eg_limit = 2
print(Solution().numberOfStableArrays(eg_zero, eg_one, eg_limit))
