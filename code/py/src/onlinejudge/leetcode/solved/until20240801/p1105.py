from onlinejudge.leetcode import *


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [0] + [inf] * n
        for i in range(1, 1 + n):
            x, y = 0, 0
            for j in reversed(range(i)):
                book = books[j]
                x += book[0]
                y = max(y, book[1])
                if shelfWidth < x:
                    break
                dp[i] = min(dp[i], dp[j] + y)
        return dp[-1]
