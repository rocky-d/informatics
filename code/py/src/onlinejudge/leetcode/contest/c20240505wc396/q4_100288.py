from onlinejudge.leetcode import *


class Solution:
    def minCostToEqualizeArray(self, nums: List[int], cost1: int, cost2: int) -> int:
        maxm = max(nums)
        if cost1 + cost1 <= cost2:
            return sum(maxm - num for num in nums) % 1_000_000_007
        ans = 0
        heap = [num - maxm for num in nums if maxm > num]
        heapify(heap)
        while 2 <= len(heap):
            a, b = -heappop(heap), -heappop(heap)
            minm = min(a, b)
            ans += cost2 * minm
            if a > minm:
                heappush(heap, minm - a)
            elif b > minm:
                heappush(heap, minm - b)
        if 1 == len(heap):
            ans += cost1 * -heappop(heap)
        return ans % 1_000_000_007


eg_nums = [1, 14, 14, 15]
eg_cost1 = 2
eg_cost2 = 1
print(Solution().minCostToEqualizeArray(eg_nums, eg_cost1, eg_cost2))
