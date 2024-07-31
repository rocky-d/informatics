from rockyutil.leetcode import *


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)

        @lru_cache(maxsize = None)
        def dfs(i: int) -> int:
            if i == n:
                return 0
            res = inf
            x, y = 0, 0
            for i in range(i, n):
                xi, yi = books[i]
                x += xi
                y = max(y, yi)
                if shelfWidth < x:
                    break
                res = min(res, dfs(i + 1) + y)
            return res

        return dfs(i = 0)
