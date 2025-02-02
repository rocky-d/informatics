from onlinejudge.leetcode import *


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        return min((a for a, _ in ops), default=m) * min((b for _, b in ops), default=n)
