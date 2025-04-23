from onlinejudge.leetcode import *


class Solution:
    def countLargestGroup(self, n: int) -> int:
        cnter = Counter(sum(map(int, str(num))) for num in range(1, 1 + n))
        return list(cnter.values()).count(max(cnter.values()))
