from onlinejudge.leetcode import *


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        heads = {}

        def find(x: Tuple[int, int]) -> Tuple[int, int]:
            if x == heads[x]:
                return x
            heads[x] = find(heads[x])
            return heads[x]

        for i in range(m):
            for j in range(n):
                if '1' == grid[i][j]:
                    a = i, j
                    heads[a] = a
                    if 0 <= i - 1 and '1' == grid[i - 1][j]:
                        b = i - 1, j
                        a_head, b_head = find(x = a), find(x = b)
                        if a_head != b_head:
                            heads[a] = heads[a_head] = b_head
                    if 0 <= j - 1 and '1' == grid[i][j - 1]:
                        b = i, j - 1
                        a_head, b_head = find(x = a), find(x = b)
                        if a_head != b_head:
                            heads[a] = heads[a_head] = b_head
        return len(frozenset(find(x = x_head) for x_head in heads.values()))


eg_grid = [
    ['1', '1', '1', '1', '0'],
    ['1', '1', '0', '1', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '0', '0', '0'],
]
print(Solution().numIslands(eg_grid))
