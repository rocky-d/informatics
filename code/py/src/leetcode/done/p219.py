from rockyutil.leetcode import *


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        idxes = {}
        for idx, num in enumerate(nums):
            if num in idxes.keys() and idx - idxes[num] <= k:
                ans = True
                break
            idxes[num] = idx
        else:
            ans = False
        return ans
