from onlinejudge.leetcode import *


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-gift for gift in gifts]
        heapify(heap)
        for _ in range(k):
            heapreplace(heap, -isqrt(-heap[0]))
        return -sum(heap)


eg_gifts = [54, 6, 34, 66, 33, 69, 43, 61, 72]
eg_k = 7
print(Solution().pickGifts(eg_gifts, eg_k))
