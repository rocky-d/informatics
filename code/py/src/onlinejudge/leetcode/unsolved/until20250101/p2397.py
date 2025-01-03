from onlinejudge.leetcode import *


class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        ans = 0
        m, n = len(matrix), len(matrix[0])

        def dfs(depth: int, free_cols: list[int]):
            nonlocal ans
            if 0 == depth:
                rows_having_1_free_cols = set()
                for col in free_cols:
                    for row in range(m):
                        if 1 == matrix[row][col]:
                            rows_having_1_free_cols.add(row)
                ans = max(ans, m - len(rows_having_1_free_cols))
            else:
                depth -= 1
                for i in range(len(free_cols)):
                    dfs(depth = depth, free_cols = free_cols[:i] + free_cols[i + 1:])

        dfs(depth = numSelect, free_cols = list(range(n)))
        return ans


eg_matrix = [
    [0, 0, 0],
    [1, 0, 1],
    [0, 1, 1],
    [0, 0, 1],
]
eg_Select = 2
print(Solution().maximumRows(eg_matrix, eg_Select))
