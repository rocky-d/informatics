from onlinejudge.leetcode import *


class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        for lft in range(n):
            for rit in range(lft + indexDifference, n):
                if valueDifference <= abs(nums[lft] - nums[rit]):
                    ans = [lft, rit]
                    break
            else:
                continue
            break
        else:
            ans = [-1, -1]
        return ans
