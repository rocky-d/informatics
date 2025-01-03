from onlinejudge.leetcode import *


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        ans = [[...] * m for _ in range(n)]
        for i, row in zip(reversed(range(m)), box):
            for j, cell in enumerate(row):
                if '*' == cell:
                    ans[j][i] = '*'
            j = -1
            for group in reversed(''.join(row).split('*')):
                if '' == group:
                    continue
                stones = group.count('#')
                while '*' == ans[j][i]:
                    j -= 1
                for _ in range(stones):
                    ans[j][i] = '#'
                    j -= 1
                for _ in range(stones, len(group)):
                    ans[j][i] = '.'
                    j -= 1
        return ans
