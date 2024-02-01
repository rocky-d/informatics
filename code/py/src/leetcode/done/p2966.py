from rockyutil.leetcode import *


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(0, len(nums), 3):
            if k < nums[i + 2] - nums[i]:
                ans = []
                break
            else:
                ans.append([nums[i], nums[i + 1], nums[i + 2]])
        return ans
