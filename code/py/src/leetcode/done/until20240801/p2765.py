from rockyutil.leetcode import *


class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 1
        i = 0
        while i < n:
            len_ = 1
            gap = 1
            tag = False
            i += 1
            while i < n and gap == nums[i] - nums[i - 1]:
                len_ += 1
                gap = -gap
                tag = True
                i += 1
            ans = max(ans, len_)
            if tag:
                i -= 1
        return -1 if 1 == ans else ans


eg_nums = [2, 3, 4, 3, 4]
print(Solution().alternatingSubarray(nums = eg_nums))
