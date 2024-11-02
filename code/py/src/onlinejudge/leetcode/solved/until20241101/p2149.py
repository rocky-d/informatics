from onlinejudge.leetcode import *


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = []
        i = j = 0
        for _ in range(len(nums) // 2):
            while nums[i] < 0:  # while not 0 < nums[i]:
                i += 1
            ans.append(nums[i])
            i += 1
            while 0 < nums[j]:  # while not nums[j] < 0:
                j += 1
            ans.append(nums[j])
            j += 1
        return ans
