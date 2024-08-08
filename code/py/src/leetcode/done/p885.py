from rockyutil.leetcode import *


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        ans = [[rStart, cStart]]
        vis = {(rStart, cStart)}
        row, col = rStart, cStart
        dirs1 = cycle(((0, +1), (+1, 0), (0, -1), (-1, 0)))
        dirs2 = cycle(((+1, 0), (0, -1), (-1, 0), (0, +1)))
        cells = rows * cols
        while len(ans) < cells:
            dx1, dy1 = next(dirs1)
            dx2, dy2 = next(dirs2)
            row += dx1
            col += dy1
            if 0 <= row < rows and 0 <= col < cols:
                ans.append([row, col])
                vis.add((row, col))
            while (row + dx2, col + dy2) in vis:
                row += dx1
                col += dy1
                if 0 <= row < rows and 0 <= col < cols:
                    ans.append([row, col])
                    vis.add((row, col))
        return ans


eg_rows = 5
eg_cols = 6
eg_rStart = 1
eg_cStart = 4
print(Solution().spiralMatrixIII(eg_rows, eg_cols, eg_rStart, eg_cStart))
