from onlinejudge.leetcode import *


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        heapify(nums)
        while nums[0] < k:
            x = heappop(nums)
            heapreplace(nums, (x << 1) + nums[0])
            ans += 1
        return ans
