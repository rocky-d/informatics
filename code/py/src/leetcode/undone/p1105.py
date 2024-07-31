from rockyutil.leetcode import *


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)

        @lru_cache(maxsize = None)
        def dfs(i: int, x: int, y: int, height: int) -> int:
            if i == n:
                return height
            book = books[i]
            i += 1
            res = dfs(i, book[0], book[1], height + book[1])
            if x + book[0] <= shelfWidth:
                dy = max(0, book[1] - y)
                res = min(res, dfs(i, x + book[0], y + dy, height + dy))
            return res

        return dfs(i = 0, x = 0, y = 0, height = 0)
