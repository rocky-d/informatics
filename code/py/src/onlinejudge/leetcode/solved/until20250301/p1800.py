from onlinejudge.leetcode import *


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = 0
        idx, n = 0, len(nums)
        while idx < n:
            curr = nums[idx]
            idx += 1
            while idx < n and nums[idx - 1] < nums[idx]:
                curr += nums[idx]
                idx += 1
            ans = max(ans, curr)
        return ans


eg_nums = [10, 20, 30, 5, 10, 50]
print(Solution().maxAscendingSum(eg_nums))
