from rockyutil.leetcode import *


class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        n = len(num2)
        num1 = num1.zfill(n)  # 补前导零，和 num2 对齐

        @cache
        def dfs(i: int, s: int, limit_low: bool, limit_high: bool) -> int:
            if s > max_sum:  # 非法
                return 0
            if i == n:
                return s >= min_sum
            lo = int(num1[i]) if limit_low else 0
            hi = int(num2[i]) if limit_high else 9
            res = 0
            for d in range(lo, hi + 1):  # 枚举当前数位填 d
                res += dfs(i + 1, s + d, limit_low and d == lo, limit_high and d == hi)
            return res

        return dfs(0, 0, True, True) % 1_000_000_007
