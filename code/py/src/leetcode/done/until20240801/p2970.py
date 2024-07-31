from rockyutil.leetcode import *


class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        if all(lst < nxt for lst, nxt in pairwise(nums)):
            return comb(len(nums) + 1, 2)
        ans = 0
        lst_lft = -1
        for lft in chain([lst_lft + 1], nums):
            if lst_lft < lft:
                lst_lft = lft
                lst_rit = 52
                for rit in chain([lst_rit - 1], reversed(nums)):
                    if lft < rit < lst_rit:
                        lst_rit = rit
                        ans += 1
                    else:
                        break
            else:
                break
        return ans
