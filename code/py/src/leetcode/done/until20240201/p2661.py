from rockyutil.leetcode import *


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        len_arr = m * n

        ans = -1
        p = [0, 0]
        memo: List[List[int]] = [[] for _i in range(1 + len_arr)]
        row_cnt, col_cnt = [0 for _i in range(m)], [0 for _i in range(n)]

        for i, arr_i in enumerate(arr):
            if 0 == len(memo[arr_i]):
                while arr_i != mat[p[0]][p[1]]:
                    memo[mat[p[0]][p[1]]] = [p[0], p[1]]
                    if p[1] + 1 < n:
                        p[1] += 1
                    else:
                        p[0] += 1
                        p[1] = 0
                else:
                    x, y = p[0], p[1]
                    if n == 1 + row_cnt[x] or m == 1 + col_cnt[y]:
                        ans = i
                        break
                    else:
                        row_cnt[x] += 1
                        col_cnt[y] += 1
            else:
                x, y = memo[arr_i][0], memo[arr_i][1]
                if n == 1 + row_cnt[x] or m == 1 + col_cnt[y]:
                    ans = i
                    break
                else:
                    row_cnt[x] += 1
                    col_cnt[y] += 1
        return ans


sol = Solution()

eg_arr = [1, 4, 5, 2, 6, 3]
eg_mat = [[4, 3, 5], [1, 2, 6]]
print(sol.firstCompleteIndex(arr = eg_arr, mat = eg_mat))
