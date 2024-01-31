from rockyutil.leetcode import *


class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        m, n = len(matrix), len(matrix[0])

        def dfs(depth: int, free_cols: list[int]):
            if 0 == depth:
                rows_having_1_free_cols = set()
                for c in free_cols:
                    for r in range(m):
                        if 1 == matrix[r][c]:
                            rows_having_1_free_cols.add(r)
                nonlocal ans
                ans = max(ans, m - len(rows_having_1_free_cols))
            else:
                depth -= 1
                for c in range(len(free_cols)):
                    dfs(depth, free_cols[:c] + free_cols[c + 1:])

        ans = 0
        dfs(numSelect, list(range(n)))
        return ans


eg_matrix = [
    [0, 0, 0],
    [1, 0, 1],
    [0, 1, 1],
    [0, 0, 1]
]
eg_Select = 2
print(Solution().maximumRows(matrix = eg_matrix, numSelect = eg_Select))
