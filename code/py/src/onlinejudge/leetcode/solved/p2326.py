from onlinejudge.leetcode import *


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        ans = [[-1] * n for _ in range(m)]
        dirs, d = ((0, +1), (+1, 0), (0, -1), (-1, 0)), 0
        x, y = 0, 0
        vis = [[False] * n for _ in range(m)]
        while head is not None:
            vis[x][y] = True
            ans[x][y] = head.val
            head = head.next
            vx, vy = x + dirs[d][0], y + dirs[d][1]
            if not (0 <= vx < m and 0 <= vy < n) or vis[vx][vy]:
                d = (d + 1) % 4
                vx, vy = x + dirs[d][0], y + dirs[d][1]
            x, y = vx, vy
        return ans


eg_m, eg_n = 3, 5
eg_head = link([3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0])
print(Solution().spiralMatrix(eg_m, eg_n, eg_head))
