from onlinejudge.leetcode import *


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(0, num, idx) for idx, num in enumerate(nums)]
        heapify(heap)
        for _ in range(k):
            cnt, num, idx = heappop(heap)
            num *= multiplier
            if 1_000_000_007 < num:
                a, num = divmod(num, 1_000_000_007)
                cnt += a
            heappush(heap, (cnt, num, idx))
        for cnt, num, idx in heap:
            nums[idx] = num
        return nums
