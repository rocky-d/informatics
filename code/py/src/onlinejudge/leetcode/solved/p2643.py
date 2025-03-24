from onlinejudge.leetcode import *


class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ans = [-1, -1]
        for i, row in enumerate(mat):
            cnt = row.count(1)
            if ans[1] < cnt:
                ans[0] = i
                ans[1] = cnt
        return ans
