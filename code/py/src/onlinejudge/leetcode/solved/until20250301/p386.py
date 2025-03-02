from onlinejudge.leetcode import *


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return sorted(range(n, 0, -1), key=str)
