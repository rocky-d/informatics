from rockyutil.leetcode import *


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        length = min(len(nums), k + 1)
        for rit in range(length):
            if nums[rit] in seen:
                ans = True
                break
            seen.add(nums[rit])
        else:
            for lft, rit in zip(range(len(nums) - length), range(length, len(nums))):
                seen.remove(nums[lft])
                if nums[rit] in seen:
                    ans = True
                    break
                seen.add(nums[rit])
            else:
                ans = False
        return ans
