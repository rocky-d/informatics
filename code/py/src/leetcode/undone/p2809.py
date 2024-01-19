from rockyutil.leetcode import *


class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        n = len(nums1)
        dp = [0 for _ in range(1 + n)]
        for i, (num2, num1) in enumerate(sorted(zip(nums2, nums1)), 1):
            for j in range(i, 0, -1):
                dp[j] = max(dp[j], dp[j - 1] + j * num2 + num1)
        nums1_sum, nums2_sum = sum(nums1), sum(nums2)
        for i in range(1 + n):
            if nums2_sum * i + nums1_sum - dp[i] <= x:
                ans = i
                break
        else:
            ans = -1
        return ans
