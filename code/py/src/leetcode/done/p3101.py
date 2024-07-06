from rockyutil.leetcode import *


class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        ans = 0
        cnt = 1
        for lst, nxt in pairwise(nums):
            if lst == nxt:
                ans += cnt * (cnt + 1) // 2
                cnt = 0
            cnt += 1
        ans += cnt * (cnt + 1) // 2
        return ans
