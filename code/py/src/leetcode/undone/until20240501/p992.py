from rockyutil.leetcode import *


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        cnter = Counter()
        lft, rit = 0, 0
        cnter[nums[rit]] += 1
        while rit < n:
            while k <= len(cnter.keys()):
                cnter[nums[lft]] -= 1
                if 0 == cnter[nums[lft]]:
                    del cnter[nums[lft]]
                lft += 1

            while len(cnter.keys()) < k:
                rit += 1
                if rit == n:
                    break
                cnter[nums[rit]] += 1
            print(lft, rit)

        return ans


eg_nums = [1, 2, 1, 2, 3]
eg_k = 2
print(Solution().subarraysWithKDistinct(eg_nums, eg_k))
