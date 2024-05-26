from rockyutil.leetcode import *


class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        vals = []
        prefs = [[0b0] + [0b0 for _ in matrix[0]]] + [[0b0] for _ in matrix]
        for i, row in enumerate(matrix, 1):
            for j, val in enumerate(row, 1):
                prefs[i].append(val ^ prefs[i - 1][j - 1] ^ prefs[i - 1][j] ^ prefs[i][j - 1])
                vals.append(prefs[i][j])
        return sorted(vals)[-k]
