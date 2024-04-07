from rockyutil.leetcode import *


class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        ans = 0
        heap_max, heap_min = [], nums
        heapify(heap_min)
        for _ in range(len(heap_min) // 2):
            heappush(heap_max, -heappop(heap_min))
        while k != heap_min[0]:
            ans += abs(k - heappop(heap_min))
            heappush(heap_min, -heappushpop(heap_max, -k))
        return ans
