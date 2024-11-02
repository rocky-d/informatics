from onlinejudge.leetcode import *


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        prefs = list(accumulate(piles, initial = 0))

        @lru_cache(maxsize = None)
        def alice(i: int, m: int) -> int:
            if i == n:
                return 0
            res = -inf
            pref = prefs[i]
            for x in range(1, m + 1):
                ix = i + x
                if n < ix:
                    break
                res = max(res, prefs[ix] - pref + bob(ix, m))
            for x in range(m + 1, m + m + 1):
                ix = i + x
                if n < ix:
                    break
                res = max(res, prefs[ix] - pref + bob(ix, x))
            return res

        @lru_cache(maxsize = None)
        def bob(i: int, m: int) -> int:
            if i == n:
                return 0
            res = inf
            for x in range(1, m + 1):
                ix = i + x
                if n < ix:
                    break
                res = min(res, alice(ix, m))
            for x in range(m + 1, m + m + 1):
                ix = i + x
                if n < ix:
                    break
                res = min(res, alice(ix, x))
            return res

        return alice(i = 0, m = 1)
