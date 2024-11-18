from onlinejudge.leetcode import *


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ans = []
        m, n = len(img), len(img[0])
        for i in range(m):
            res = []
            for j in range(n):
                cells, sum_cells = 1, img[i][j]
                for dx, dy in (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1):
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n:
                        cells += 1
                        sum_cells += img[x][y]
                res.append(math.floor(sum_cells / cells))
            ans.append(res)
        return ans
