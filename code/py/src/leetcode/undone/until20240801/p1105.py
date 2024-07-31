from rockyutil.leetcode import *


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)

        @lru_cache(maxsize = None)
        def dfs(i: int, x: int, y: int, height: int) -> int:
            if i == n:
                return height + y
            xi, yi = books[i]
            i += 1
            res = dfs(i, xi, yi, height + y)
            if x + xi <= shelfWidth:
                res = min(res, dfs(i, x + xi, max(y, yi), height))
            return res

        return dfs(i = 0, x = 0, y = 0, height = 0)
