from rockyutil.leetcode import *


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        nums_counter = Counter(nums)
        ans = max(1, nums_counter[1] if 0b1 == 0b1 & nums_counter[1] else nums_counter[1] - 1)
        dp = dict()
        for num in sorted(nums_counter.keys(), reverse = True):
            num_square = num * num
            if 2 <= nums_counter[num] and num_square in dp.keys():
                dp[num] = 2 + dp[num_square]
                ans = max(ans, dp[num])
            else:
                dp[num] = 1
        return ans


eg_nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
print(Solution().maximumLength(nums = eg_nums))
