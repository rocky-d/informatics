from rockyutil.leetcode import *


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ans = n = len(nums)
        lft, rit = 0, nums.count(1) - 1
        zeros = sum(1 for i in range(lft, rit + 1) if 0 == nums[i])
        for _ in range(n):
            ans = min(ans, zeros)
            if 0 == nums[lft]:
                zeros -= 1
            lft = (lft + 1) % n
            rit = (rit + 1) % n
            if 0 == nums[rit]:
                zeros += 1
        return ans


eg_nums = [0, 1, 1, 1, 0, 0, 1, 1, 0]
print(Solution().minSwaps(eg_nums))
