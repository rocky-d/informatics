from onlinejudge.leetcode import *


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(num, idx) for idx, num in enumerate(nums)]
        heapify(heap)
        for _ in range(k):
            num, idx = heappop(heap)
            num *= multiplier
            heappush(heap, (num, idx))
        for num, idx in heap:
            nums[idx] = num
        return nums
