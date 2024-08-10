from onlinejudge.leetcode import *


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = mean * (len(rolls) + n) - sum(rolls)
        low = total // n
        upps = total - low * n
        return [] if low < 1 or 6 == low and 0 < upps or 6 < low else [low] * (n - upps) + [low + 1] * upps
