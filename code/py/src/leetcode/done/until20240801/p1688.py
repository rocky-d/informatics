import math


class Solution:
    def numberOfMatches(self, n: int) -> int:
        ans = 0
        while 1 < n:
            ans += n // 2
            n = math.ceil(n / 2)
        return ans
