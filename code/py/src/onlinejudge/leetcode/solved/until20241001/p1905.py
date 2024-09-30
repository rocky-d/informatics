from onlinejudge.leetcode import *


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ans = 0
        m, n = len(grid1), len(grid1[0])
        vis = [[False] * n for _ in range(m)]
        for i, j in product(range(m), range(n)):
            if 1 == grid2[i][j] and not vis[i][j]:
                island = True
                vis[i][j] = True
                que = deque([(i, j)])
                while 0 < len(que):
                    ux, uy = que.popleft()
                    if 0 == grid1[ux][uy]:
                        island = False
                    for dx, dy in (0, -1), (-1, 0), (0, +1), (+1, 0):
                        vx, vy = ux + dx, uy + dy
                        if 0 <= vx < m and 0 <= vy < n and 1 == grid2[vx][vy] and not vis[vx][vy]:
                            vis[vx][vy] = True
                            que.append((vx, vy))
                if island:
                    ans += 1
        return ans
