from onlinejudge.leetcode import *


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        board_cnter = Counter(chain(*board))
        if any(board_cnter[char] < cnt for char, cnt in Counter(word).items()):
            return False
        if board_cnter[word[-1]] < board_cnter[word[0]]:
            word = word[::-1]
        m, n = len(board), len(board[0])
        word_len = len(word)
        seen = set()

        def dfs(x: int, y: int, idx: int) -> bool:
            idx += 1
            if idx == word_len:
                return True
            seen.add((x, y))
            for oft_x, oft_y in (0, -1), (0, +1), (-1, 0), (+1, 0):
                nxt_x, nxt_y = x + oft_x, y + oft_y
                if 0 <= nxt_x < m and 0 <= nxt_y < n and (nxt_x, nxt_y) not in seen and word[idx] == board[nxt_x][nxt_y]:
                    if dfs(nxt_x, nxt_y, idx):
                        res = True
                        break
            else:
                res = False
            seen.remove((x, y))
            return res

        for i, j in product(range(m), range(n)):
            if word[0] == board[i][j]:
                if dfs(x = i, y = j, idx = 0):
                    ans = True
                    break
        else:
            ans = False
        return ans
