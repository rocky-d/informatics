from onlinejudge.leetcode import *


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        t = 0
        que = deque(((i, j), t) for i in range(m) for j in range(n) if 2 == grid[i][j])
        while 0 < len(que):
            (x, y), t = que.popleft()
            t_nxt = t + 1
            for x_nxt, y_nxt in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
                if 0 <= x_nxt < m and 0 <= y_nxt < n:
                    if 1 == grid[x_nxt][y_nxt]:
                        grid[x_nxt][y_nxt] = 2
                        que.append(((x_nxt, y_nxt), t_nxt))
        return -1 if any(1 == grid[i][j] for i in range(m) for j in range(n)) else t
