from onlinejudge.leetcode import *


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        maxi, cnt = max(nums), 0
        lft, rit = 0, 0
        if maxi == nums[rit]:
            cnt += 1
        while True:
            while k <= cnt:
                if maxi == nums[lft]:
                    cnt -= 1
                lft += 1
            while cnt < k:
                ans += lft
                rit += 1
                if rit == n:
                    break
                if maxi == nums[rit]:
                    cnt += 1
            else:
                continue
            break
        return ans
