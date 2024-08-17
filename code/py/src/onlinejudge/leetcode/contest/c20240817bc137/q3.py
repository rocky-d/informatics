from onlinejudge.leetcode import *


class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        ans = -3_000_000_000
        m_1 = len(board) - 1

        @lru_cache(maxsize = None)
        def dfs(row: int, total: int, vis: int) -> None:
            nonlocal ans
            if 3 == vis.bit_count():
                ans = max(ans, total)
                return
            if row == m_1:
                return
            row += 1
            dfs(row, total, vis)
            for col, val in enumerate(board[row]):
                if 0b1 == 0b1 & (vis >> col):
                    continue
                mask = 0b1 << col
                vis |= mask
                dfs(row, total + val, vis)
                vis &= ~mask

        dfs(row = -1, total = 0, vis = 0b0)
        return ans


eg_board = [
    [-3, 1, 1, 1],
    [-3, 1, -3, 1],
    [-3, 2, 1, 1],
]
print(Solution().maximumValueSum(eg_board))
