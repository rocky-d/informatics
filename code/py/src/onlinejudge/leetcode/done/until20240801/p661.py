from onlinejudge.leetcode import *


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        ans = []
        for i in range(m):
            ans.append([])
            for j in range(n):
                cells, sum_cells = 1, img[i][j]
                for x_offset, y_offset in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
                    x, y = i + x_offset, j + y_offset
                    if -1 < x < m and -1 < y < n:
                        cells += 1
                        sum_cells += img[x][y]
                ans[-1].append(math.floor(sum_cells / cells))
        return ans
