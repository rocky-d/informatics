from onlinejudge.leetcode import *


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        m, n = len(matrix), len(matrix[0])
        (x_lft, x_rit), (y_lft, y_rit) = (1, m - 1), (0, n - 1)
        x, y = 0, 0
        direction = 0, 1
        for _ in range(m * n):
            ans.append(matrix[x][y])
            if (0, 1) == direction and y == y_rit:
                y_rit -= 1
                direction = 1, 0
            elif (1, 0) == direction and x == x_rit:
                x_rit -= 1
                direction = 0, -1
            elif (0, -1) == direction and y_lft == y:
                y_lft += 1
                direction = -1, 0
            elif (-1, 0) == direction and x_lft == x:
                x_lft += 1
                direction = 0, 1
            x += direction[0]
            y += direction[1]
        return ans
