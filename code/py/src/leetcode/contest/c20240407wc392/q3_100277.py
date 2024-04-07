from rockyutil.leetcode import *


class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        heapify(nums)
        heap_max, heap_min = [], []
        for _ in range(n // 2):
            heappush(heap_max, -heappop(nums))
        heap_min = nums
        while True:
            mid = heappop(heap_min)
            if mid == k:
                break
            elif mid < k:
                ans += k - mid
                mid = k
                heappush(heap_min, mid)
            else:
                ans += mid - k
                mid = k
                heappush(heap_min, -heappushpop(heap_max, -mid))
        return ans
