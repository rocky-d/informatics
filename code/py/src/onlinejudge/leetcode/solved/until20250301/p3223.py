from onlinejudge.leetcode import *


class Solution:
    def minimumLength(self, s: str) -> int:
        return sum(min(1 if 0b1 == 0b1 & cnt else 2, cnt) for cnt in Counter(s).values())
