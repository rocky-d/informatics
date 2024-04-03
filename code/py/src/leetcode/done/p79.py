from rockyutil.leetcode import *


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        word_len = len(word)
        seen = set()

        def dfs(idx: int, x: int, y: int) -> bool:
            if idx == word_len - 1:
                return True
            seen.add((x, y))
            for oft_x, oft_y in (0, -1), (0, +1), (-1, 0), (+1, 0):
                x_nxt, y_nxt = x + oft_x, y + oft_y
                if 0 <= x_nxt < m and 0 <= y_nxt < n and (x_nxt, y_nxt) not in seen and word[idx + 1] == board[x_nxt][y_nxt]:
                    if dfs(idx + 1, x_nxt, y_nxt):
                        res = True
                        break
            else:
                res = False
            seen.remove((x, y))
            return res

        for i, j in product(range(m), range(n)):
            if word[0] == board[i][j]:
                if dfs(idx = 0, x = i, y = j):
                    ans = True
                    break
        else:
            ans = False
        return ans
