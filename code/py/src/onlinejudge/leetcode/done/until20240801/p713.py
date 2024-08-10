from onlinejudge.leetcode import *


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = 0
        cnt = 1
        lft = 0
        for rit, num in enumerate(nums):
            cnt *= num
            while lft <= rit and k <= cnt:
                cnt //= nums[lft]
                lft += 1
            ans += rit - lft + 1
        return ans


eg_nums = [10, 5, 2, 6]
eg_k = 100
print(Solution().numSubarrayProductLessThanK(eg_nums, eg_k))
