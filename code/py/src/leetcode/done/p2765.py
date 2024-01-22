from rockyutil.leetcode import *


class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -1
        i = 0
        while i < n:
            len_ = 1
            gap = 1
            tag = False
            while i + 1 < n and gap == nums[i + 1] - nums[i]:
                len_ += 1
                gap = -gap
                i += 1
                tag = True
            if not tag:
                i += 1
            ans = max(ans, len_)
        if 1 == ans:
            ans = -1
        return ans


eg_nums = [2, 3, 4, 3, 4]
print(Solution().alternatingSubarray(nums = eg_nums))
