from onlinejudge.leetcode import *


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for _ in range(1, numRows):
            ans.append([ans[-1][0]] + [lst + nxt for lst, nxt in pairwise(ans[-1])] + [ans[-1][-1]])
        return ans
