from leetcode.util import *


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        empty_ls = [False for _ in range(9)]
        ls = empty_ls.copy()
        for i in range(9):
            ...
