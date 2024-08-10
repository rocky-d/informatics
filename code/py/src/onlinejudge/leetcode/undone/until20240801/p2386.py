from onlinejudge.leetcode import *


class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        total = 0
        for i in range(n):
            if nums[i] >= 0:
                total += nums[i]
            else:
                nums[i] = -nums[i]
        nums.sort()
        ret = 0
        pq = [(nums[0], 0)]
        for j in range(2, k + 1):
            t, i = heappop(pq)
            ret = t
            if i == n - 1:
                continue
            heappush(pq, (t + nums[i + 1], i + 1))
            heappush(pq, (t - nums[i] + nums[i + 1], i + 1))
        return total - ret
