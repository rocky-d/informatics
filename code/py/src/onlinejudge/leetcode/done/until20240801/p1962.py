from onlinejudge.leetcode import *


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        minus_piles = [-pile for pile in piles]
        heapq.heapify(minus_piles)
        for _ in range(k):
            heapq.heappush(minus_piles, math.floor(heapq.heappop(minus_piles) / 2))
        return -sum(minus_piles)


eg_piles = [5, 4, 9]
eg_k = 2
print(Solution().minStoneSum(piles = eg_piles, k = eg_k))
