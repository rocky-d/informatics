from onlinejudge.leetcode import *


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        return Counter(tuple(row if 0 == row[0] else (1 - cell for cell in row)) for row in matrix).most_common(n=1)[0][1]
