from onlinejudge.leetcode import *


class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        return 'Alice' if 0b1 == 0b1 & min(x, y // 4) else 'Bob'
