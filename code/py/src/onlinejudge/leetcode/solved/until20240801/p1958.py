from onlinejudge.leetcode import *


class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        color_reversed = {'W': 'B', 'B': 'W'}[color]

        def direction(x: int, y: int) -> bool:
            segment = color
            r, c = rMove + x, cMove + y
            while 0 <= r < 8 and 0 <= c < 8 and '.' != board[r][c]:
                segment += board[r][c]
                r += x
                c += y
            return any(color == segment[i] and all(color_reversed == segment[j] for j in range(1, i)) for i in range(2, len(segment)))

        return any(direction(x = x, y = y) for x, y in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)))
