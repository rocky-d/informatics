from rockyutil.leetcode import *


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ans = n = len(nums)
        lft, rit = 0, nums.count(0) - 1
        ones = sum(1 for i in range(lft, rit + 1) if 1 == nums[i])
        for _ in range(n):
            ans = min(ans, ones)
            if 1 == nums[lft]:
                ones -= 1
            lft = (lft + 1) % n
            rit = (rit + 1) % n
            if 1 == nums[rit]:
                ones += 1
        return ans


eg_nums = [0, 1, 1, 1, 0, 0, 1, 1, 0]
print(Solution().minSwaps(eg_nums))
