from rockyutil.leetcode import *


class Solution:
    def guessNumber(self, n: int) -> int:
        return bisect_left(range(n + 1), 0, lo = 1, key = lambda mid: -guess(mid))
