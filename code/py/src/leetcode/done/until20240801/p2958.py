from rockyutil.leetcode import *


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = 1
        n = len(nums)
        lft, rit = 0, 0
        cnter = Counter([nums[0]])
        while rit < n:
            while k < cnter[nums[rit]]:
                cnter[nums[lft]] -= 1
                lft += 1
            while cnter[nums[rit]] <= k:
                rit += 1
                if rit == n:
                    ans = max(ans, rit - lft)
                    break
                cnter[nums[rit]] += 1
            ans = max(ans, rit - lft)
        return ans


eg_nums = [1, 2, 3, 1, 2, 3, 1, 2]
eg_k = 2
print(Solution().maxSubarrayLength(eg_nums, eg_k))
