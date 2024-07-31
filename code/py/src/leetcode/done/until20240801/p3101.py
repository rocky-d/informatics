from rockyutil.leetcode import *


class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        ans = 0
        cnt = 2
        for lst, nxt in pairwise(nums):
            if lst == nxt:
                ans += comb(cnt, 2)
                cnt = 1
            cnt += 1
        ans += comb(cnt, 2)
        return ans
