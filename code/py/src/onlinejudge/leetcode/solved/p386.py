from onlinejudge.leetcode import *


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return list(map(int, sorted(map(str, range(n, 0, -1)))))
