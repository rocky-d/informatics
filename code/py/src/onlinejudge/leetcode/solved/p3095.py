from onlinejudge.leetcode import *


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        for leng in range(1, 1 + n):
            for lft in range(n - leng + 1):
                if k <= reduce(or_, nums[lft : lft + leng]):
                    ans = leng
                    break
            else:
                continue
            break
        else:
            ans = -1
        return ans
