from onlinejudge.leetcode import *


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if 1 == mat[i][j]:
                    ones = 0
                    for ii in range(m):
                        if 1 == mat[ii][j]:
                            ones += 1
                            if 1 < ones:
                                break
                    else:
                        ones = 0
                        for jj in range(n):
                            if 1 == mat[i][jj]:
                                ones += 1
                                if 1 < ones:
                                    break
                        else:
                            ans += 1
        return ans
